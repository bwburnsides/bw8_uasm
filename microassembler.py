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
    base: ...

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        return self


def Instruction(*, base=None):
    def wrapper(func):
        return _Instruction(func, base=None)

    return wrapper


class OpcodeMeta(type):
    def __getattribute__(cls, name):
        # print(f"OpcodeMeta.__getattribute__({name})")

        opcodes = super().__getattribute__("_OPCODES")

        if name not in opcodes:
            _add_opcode = super().__getattribute__("_add_opcode")
            _add_opcode(name)

        return opcodes[name]

    def __setattr__(cls, name: str, value: Any) -> None:
        # print(f"OpcodeMeta.__setattr__({name}, {value})")

        if not isinstance(value, _Instruction):
            return

        opcodes = super().__getattribute__("_OPCODES")
        if name not in opcodes:
            print(f"Opcode {name} does not exist.")
            exit()

        opcodes[name]._definition = value

    def _add_opcode(cls, name: str):
        opcodes = super().__getattribute__("_OPCODES")
        opcodes[name] = cls(name)


# TODO: This class needs to be dynamically created
# based on state information provided by the user.
# TODO TODO: or should it 🤔
class Opcode(metaclass=OpcodeMeta):
    _OPCODES = {}

    def __init__(self, name: str, Extended: bool = False):
        # print(f"Opcode.__init__({name}, {Extended=})")

        self.name = name
        self.Extended = Extended

        self._definition = None

    def _existed(self):
        existed = hasattr(self, "_initialized") and self._initialized == True
        self._initialized = True
        return existed

    def __call__(self, Extended: bool = False):
        # print(f"Opcode.__call__({Extended=})")

        if self._existed():
            print(f"Redefinition of Opcode {self.name}")
            exit()

        self.Extended = Extended

    def __repr__(self) -> str:
        class_name = object.__getattribute__(self.__class__, "__name__")
        name = self.name
        Extended = self.Extended

        return f"{class_name}({name=}, {Extended=})"
