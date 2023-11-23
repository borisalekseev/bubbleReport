import os


FILES_DIR_NAME = "test_data"
FILES_PATH = os.path.join(os.path.abspath(""), FILES_DIR_NAME)
COLUMNS = {
    "scheme_cart_cond_id": "scheme_cart_cond_id",
    "intermediate_id_intr": "intermediate_id",
    "scheme_cart_id": "scheme_cart_id",
    "scheme_id": "scheme_id",
    "compound_id": "compound_id(from scc)",
    "stage_reagent_cond_id": "stage_reagent_cond_id",
    "category": "category",
    "reagent_category": "reagent_category",
    "reagent_type": "reagent_type",
    "inn_eng": "API",
    "cas_interm_c": "CAS",
    "title_name_interm_c": "title_name",
    "number": "Var",
    "name": "stage name",
    "stage_number": "stage number",
    "title_name": "Substance",
    "cas": "substance_CAS",
    "mw_g_mol": "Mr",
    "priority": "priority",
    "ratio_stage_prod_mass_rkms": "Consumption coefficient, kg/kg SP",
    "rkms_stage": "Consumption coefficient, kg/kg TP",
    "ratio_stage_prod_mass_rkms_src":  "Consumption coefficient, kg/kg SP WHEN SCC NULL",
    "ratio_target_prod": "Consumption coefficient, kg/kg TP  WHEN SCC NULL",
    "chemical_processes_1": "chemical_processes_1",
    "chemical_processes_2": "chemical_processes_2"
}