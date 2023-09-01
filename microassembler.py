import enum
from copy import deepcopy
import sys
import dataclasses


class _BaseField(enum.IntEnum):
    def __call__(self, new_value):
        setattr(
            self.owner,
            self.__class__.__name__,
            self.__class__(new_value),
        )

        return self.owner


class Field:
    def __class_getitem__(self, width: int):
        class _Field(_BaseField):
            @staticmethod
            def _generate_next_value_(name, start, count, last_values):
                assert count < (2**width)
                return count

        _Field._WIDTH = width
        return _Field


Field.encode = enum.auto


class Bus:
    _WIDTH = None
    _FIELDS = {}

    def __class_getitem__(cls, width: int):
        assert Bus._WIDTH is None
        Bus._WIDTH = width
        return cls

    def __init__(self, *fields):
        assert Bus._WIDTH is not None
        assert all(issubclass(field, _BaseField) for field in fields)
        assert sum(field._WIDTH for field in fields) <= Bus._WIDTH
        Bus._FIELDS = fields

        _create_microinstruction(Bus._FIELDS)


def _create_microinstruction(fields):
    field_triples = ((field.__name__, field, field(0)) for field in fields)

    def __MICROINSTRUCTION__post_init__(self):
        self.LeftRegister.owner = self
        self.RightRegister.owner = self

    def __MICROINSTRUCTION__getattribute__(self, name):
        if name in fields:
            copy = deepcopy(self)
            for field in fields:
                object.__getattribute__(copy, field.__name__).owner = copy

            return object.__getattribute__(copy, name)

        return object.__getattribute__(self, name)

    MicroInstruction = dataclasses.make_dataclass(
        "MicroInstruction",
        field_triples,
        namespace={
            "__post_init__": __MICROINSTRUCTION__post_init__,
            "__getattribute__": __MICROINSTRUCTION__getattribute__,
        },
    )

    sys.modules[__name__].MicroInstruction = MicroInstruction
