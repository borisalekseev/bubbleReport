from pydantic import TypeAdapter

from .base import ReaderBase
from models import Compounds, Intermediates, SchemeCart, SchemeCartCond, Schemes, StageReagentCond, Stages

__all__ = ["CompoundsReader", "IntermediatesReader", "SchemeCartReader", "SchemeCartCondReader", "SchemesReader", "StageReagentCondReader", "StagesReader"]


class CompoundsReader(ReaderBase):
    list_parser = TypeAdapter(list[Compounds])
    pattern = r'.+All-Compounds-.+\.json'


class IntermediatesReader(ReaderBase):
    list_parser = TypeAdapter(list[Intermediates])
    pattern = r'.+DB-Intermediates.+\.json'


class SchemeCartReader(ReaderBase):
    list_parser = TypeAdapter(list[SchemeCart])
    pattern = r'.+All-scheme-carts.+\.json'


class SchemeCartCondReader(ReaderBase):
    list_parser = TypeAdapter(list[SchemeCartCond])
    pattern = r'.+All-Scheme-cart-conds.+\.json'


class SchemesReader(ReaderBase):
    list_parser = TypeAdapter(list[Schemes])
    pattern = r'.+All--Schemes.+\.json'


class StageReagentCondReader(ReaderBase):
    list_parser = TypeAdapter(list[StageReagentCond])
    pattern = r'.+Stage-reagents-conds.+\.json'


class StagesReader(ReaderBase):
    list_parser = TypeAdapter(list[Stages])
    pattern = r'.+All--Stages.+\.json'
