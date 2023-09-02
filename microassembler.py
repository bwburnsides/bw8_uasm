import enum
from copy import deepcopy
import dataclasses
from collections import namedtuple
from typing import Any


DataclassField = namedtuple("DataclassField", ("name", "hint", "default"))


class _BaseField(enum.IntEnum):
    _DEFINED_FIELDS = enum.nonmember([])

    def __init_subclass__(cls):
        if cls.__name__ != "_Field":
            _BaseField._DEFINED_FIELDS.append(cls)

    def __call__(self, new_value):
        setattr(
            self.owner,
            self.__class__.__name__,
            self.__class__(new_value),
        )

        return self.owner

    @classmethod
    def _by_name(cls, name):
        for field in cls._DEFINED_FIELDS:
            if field.__name__ == name:
                return field

        raise KeyError


class Field:
    def __class_getitem__(self, width: int):
        class _Field(_BaseField):
            _WIDTH = enum.nonmember(width)

            @staticmethod
            def _generate_next_value_(name, start, count, last_values):
                assert count < (2**width)
                return count

        return _Field


Field.encode = enum.auto


class _BaseBus(enum.IntEnum):
    ...


class Bus:
    def __class_getitem__(self, width: int):
        class _Bus(_BaseBus):
            _CURRENT_SHIFT = enum.nonmember(0)

            @staticmethod
            def _generate_next_value_(name, start, count, last_value):
                # TODO: Needs more descriptive error.
                if not any(
                    name == field.__name__ for field in _BaseField._DEFINED_FIELDS
                ):
                    print(f"{name} is not a previously defined Field.")
                    exit()

                value = _Bus._CURRENT_SHIFT
                _Bus._CURRENT_SHIFT += _BaseField._by_name(name)._WIDTH

                # TODO: Needs more descriptive error.
                if _Bus._CURRENT_SHIFT > width:
                    print("Bus width exceeded.")
                    exit()

                return value

            def __init_subclass__(cls, *args, **kwargs):
                cls.MicroInstruction = _create_microinstruction(list(cls))

        return _Bus


Bus.place = enum.auto


def _create_microinstruction(fields):
    field_triples = (
        DataclassField(
            name=field.name, hint=..., default=_BaseField._by_name(field.name)(0)
        )
        for field in fields
    )

    def __post_init__(self):
        for field in fields:
            attr = object.__getattribute__(self, field.name)
            attr.owner = self

    def __getattribute__(self, name):
        field_names = (field.name for field in fields)

        if name in field_names:
            copy = deepcopy(self)

            for field in fields:
                object.__getattribute__(copy, field.name).owner = copy

            return object.__getattribute__(copy, name)

        return object.__getattribute__(self, name)

    MicroInstruction = dataclasses.make_dataclass(
        cls_name="MicroInstruction",
        fields=field_triples,
        namespace={
            "__post_init__": __post_init__,
            "__getattribute__": __getattribute__,
        },
    )

    return MicroInstruction


@dataclasses.dataclass
class _Instruction:
    function: ...

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self


def Instruction(func):
    return _Instruction(func)


class OpcodeMeta(type):
    def __getattribute__(cls, name):
        opcodes = super().__getattribute__("_OPCODES")

        try:
            opcode = opcodes[name]
        except KeyError:
            opcode = cls(name)
            opcodes[name] = opcode

        return opcode

    def __setattr__(cls, name: str, value: Any) -> None:
        if not isinstance(value, _Instruction):
            return

        opcodes = super().__getattribute__("_OPCODES")

        try:
            opcodes[name]._definition = value
        except KeyError:
            ...


# TODO: This class needs to be dynamically created
# based on state information provided by the user.
class Opcode(metaclass=OpcodeMeta):
    _OPCODES = {}

    def __init__(self, name: str, Extended: bool = False):
        self.name = name
        self.Extended = Extended

        self._definition = None

    def __call__(self, Extended: bool):
        self.Extended = Extended

    def __repr__(self) -> str:
        class_name = object.__getattribute__(self.__class__, "__name__")
        name = self.name
        Extended = self.Extended
        return f"{class_name}({name=}, {Extended=})"

    def __setattr__(self, name: str, value: Any) -> None:
        return super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)
