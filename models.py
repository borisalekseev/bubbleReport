from pydantic import BaseModel, Field
from typing import Optional


class Compounds(BaseModel):
    compound_id: str = Field(max_length=128, alias="unique id")
    another_id: Optional[str | None] = Field(max_length=255, default=None)
    cas: Optional[str | None] = Field(max_length=45, default=None, alias="CAS")
    complexity_rating_pubchem: Optional[float | None] = None
    country_destination_id: Optional[str | None] = Field(max_length=128, default=None)
    crypt_name: Optional[str | None] = None
    density: Optional[str | None] = Field(pattern=r'(\d+(\.\d+)?)?')
    inchi: Optional[str | None] = None
    inchi_key: Optional[str | None] = None
    mol_formula: Optional[str | None] = None
    mol_image: Optional[str | None] = None
    mw_g_mol: Optional[str | None] = Field(alias="MW_g-mol")
    name_iupac: Optional[str | None] = None
    organic: Optional[str | None] = None
    other_cas: Optional[str | None] = None
    rus_name: Optional[str | None] = None
    smiles_canon: Optional[str | None] = None
    smiles_isometr: Optional[str | None] = None
    solubility_text: Optional[str | None] = None
    synonyms: Optional[str | None] = None
    t_decomposition: Optional[float | None] = None
    title_name: Optional[str | None] = Field(alias="Title_name")
    special_regulation_id: Optional[str | None] = None
    hazard_properties: Optional[str | None] = None
    viscosity: Optional[float | None] = None
    organizations_id: Optional[str | None] = None
    shareable: Optional[int | None] = None
    pubchem_cid: Optional[int | None] = None
    other_properties: Optional[str | None] = None
    name_from_source: Optional[str | None] = None
    t_bolling_max: Optional[float | None] = None
    t_bolling_min: Optional[float | None] = None
    t_flash_point_max: Optional[float | None] = None
    t_flash_point_min: Optional[float | None] = None
    t_melting_max: Optional[float | None] = None
    t_melting_min: Optional[float | None] = None

class Intermediates(BaseModel):
    intermediate_id: str = Field(max_length=128, alias="unique id")
    compound_id: str = Field(max_length=128, alias="compound")
    inn_eng: Optional[str | None] = None
    inn_rus: Optional[str | None] = None
    projects: Optional[str | None] = None
    comment: Optional[str | None] = None
    category: Optional[str | None] = None
    priority: Optional[str | None] = None
    export: Optional[str | None] = None


class SchemeCart(BaseModel):
    scheme_cart_id: str = Field(max_length=128, alias="unique id")
    disabled: Optional[str | None] = None
    intermediate_id: str = Field(max_length=128, alias="intermediate")
    name: Optional[str | None] = None
    next_stage_id: str = Field(max_length=128, alias="next_stage")
    scheme_id: str = Field(max_length=128, alias="scheme")
    scheme_cart_error: Optional[int | None] = None
    stage_id: str = Field(max_length=128, alias="stages")
    stage_main_product: Optional[int | None] = None
    stage_main_reagent: Optional[str | None] = None
    stage_number: Optional[float | None] = None
    stage_rk_re_count_coefficient: Optional[float | None] = None


class SchemeCartCond(BaseModel):
    scheme_cart_cond_id: str = Field(max_length=128, alias="unique id")
    stage_reagent_cond_id: str = Field(max_length=128, alias="stage_reag_cond")
    compound_id: str = Field(max_length=128, alias="compound")
    ratio_stage_prod_mass_rkms: str = Field(alias="ratio_stage_prod_mass(rkms)")
    rkms_stage: str = Field(alias="rkms_stage")
    scheme_cart_id: str = Field(max_length=128, alias="scheme_cart")


class Schemes(BaseModel):
    scheme_id: str = Field(max_length=128, alias="unique id")
    # cutted_stage_id: str = Field(max_length=128)
    intermediate_id: str = Field(max_length=128, alias="Intermediate")
    reagents: Optional[int | None] = None
    responsibles: Optional[str | None] = None
    comment: Optional[str | None] = None
    error: Optional[int | None] = None
    complexity: Optional[float | None] = None
    name: Optional[str | None] = None
    number: Optional[float | None] = Field(alias="scheme_number")
    png: Optional[str | None] = None
    priority: Optional[str | None] = Field(alias="scheme_priority")
    default: Optional[str | None] = None


class StageReagentCond(BaseModel):
    stage_reagent_cond_id: str = Field(max_length=128, alias="unique id")
    compound_id: str = Field(max_length=128, alias="Compound")
    mass: Optional[str | None] = None
    moles: Optional[str | None] = None
    volume: Optional[str | None] = None
    purity: Optional[str | None] = None
    yield_field: Optional[str | None] = None  # Field renamed because it was a Python reserved word.
    stage_id: Optional[str | None] = Field(max_length=128, default=None)
    comment: Optional[str | None] = None
    equiv: Optional[str | None] = None
    limiting: Optional[str | None] = None
    ratio_stage_prod_mass_rkms: str = Field(alias="ratio_stage_prod_mass(rkms)")
    ratio_target_prod: str = Field(alias="ratio_target_prod")
    spent_share: Optional[str | None] = None
    ratio_stage_prod_mol_rkmp: Optional[str | None] = Field(alias="ratio_stage_prod_mol(rkmp)")
    reagent_category: Optional[str | None] = None
    reagent_type: Optional[str | None] = None


class Stages(BaseModel):
    stage_id: str = Field(max_length=128,alias="unique id")
    chemical_processes: Optional[str | None] = None
    comment: Optional[str | None] = None
    lit_sources: Optional[str | None] = None
    description: Optional[str | None] = None
    complexity: Optional[float | None] = None
    synthesis_procedure: Optional[str | None] = None
    yield_field: Optional[float | None] = None  # Field renamed because it was a Python reserved word.
    responsible: Optional[str | None] = None
    shareable: Optional[int | None] = None
    chemical_processes_1: Optional[str | None] = Field(alias="Chemical_processes_1")
    chemical_processes_2: Optional[str | None] = Field(alias="Chemical_processes_2")
