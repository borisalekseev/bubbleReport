from pydantic import BaseModel, Field
from typing import Optional


class Compounds(BaseModel):
    compound_id: str = Field(max_length=128, alias="unique id")
    cas: Optional[str | None] = Field(max_length=45, default=None, alias="CAS")
    density: str
    mw_g_mol: Optional[str | None] = Field(alias="MW_g-mol")
    title_name: Optional[str | None] = Field(alias="Title_name")

class Intermediates(BaseModel):
    intermediate_id: str = Field(max_length=128, alias="unique id")
    compound_id: str = Field(max_length=128, alias="compound")
    inn_eng: str = Field(alias="INN_eng")
    intermediate_category: str = Field(alias="Int_category")


class SchemeCart(BaseModel):
    scheme_cart_id: str = Field(max_length=128, alias="unique id")
    intermediate_id: str = Field(max_length=128, alias="intermediate")
    next_stage_id: str = Field(max_length=128, alias="next_stage")
    scheme_id: str = Field(max_length=128, alias="scheme")
    stage_id: str = Field(max_length=128, alias="stages")
    name: str
    stage_number: str


class SchemeCartCond(BaseModel):
    scheme_cart_cond_id: str = Field(max_length=128, alias="unique id")
    stage_reagent_cond_id: str = Field(max_length=128, alias="stage_reag_cond")
    compound_id: str = Field(max_length=128, alias="compound")
    ratio_stage_prod_mass_rkms: str = Field(alias="ratio_stage_prod_mass(rkms)")
    rkms_stage: str = Field(alias="rkms_stage")
    scheme_cart_id: str = Field(max_length=128, alias="scheme_cart")


class Schemes(BaseModel):
    scheme_id: str = Field(max_length=128, alias="unique id")
    intermediate_id: str = Field(max_length=128, alias="Intermediate")
    number: Optional[float | None] = Field(alias="scheme_number")
    priority: Optional[str | None] = Field(alias="scheme_priority")


class StageReagentCond(BaseModel):
    stage_reagent_cond_id: str = Field(max_length=128, alias="unique id")
    compound_id: str = Field(max_length=128, alias="Compound")
    stage_id: Optional[str | None] = Field(max_length=128, default=None)
    ratio_stage_prod_mass_rkms: str = Field(alias="ratio_stage_prod_mass(rkms)")
    ratio_target_prod: str = Field(alias="ratio_target_prod")
    reagent_category: str
    reagent_type: str



class Stages(BaseModel):
    stage_id: str = Field(max_length=128,alias="unique id")
    chemical_processes_1: Optional[str | None] = Field(alias="Chemical_processes_1")
    chemical_processes_2: Optional[str | None] = Field(alias="Chemical_processes_2")
