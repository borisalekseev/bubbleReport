import file_readers as fr
from settings import COLUMNS
from datetime import datetime

COL_ORDER = list(COLUMNS.keys())

def main():
    scc_df = fr.SchemeCartCondReader().get_df()
    sc_df = fr.SchemeCartReader().get_df()
    scc_compounds_df = fr.CompoundsReader().get_df()
    stage_df = fr.StagesReader().get_df()
    schemes_df = fr.SchemesReader().get_df()
    intermediates_df = fr.IntermediatesReader().get_df()
    src_df = fr.StageReagentCondReader().get_df()
    compounds_df = fr.CompoundsReader().get_df()
    
    df = scc_df.set_index("scheme_cart_id", drop=False).join(
        sc_df.set_index("scheme_cart_id", drop=False), how="left", rsuffix="_sc"
    )\
    .set_index("compound_id", drop=False).join(
        scc_compounds_df.set_index("compound_id", drop=False), how="left", rsuffix="_scc_comp"
    )\
    .set_index("stage_id", drop=False).join(
        stage_df.set_index("stage_id", drop=False), how="left", rsuffix="stg_"
    )\
    .set_index("scheme_id", drop=False).join(
        schemes_df.set_index("scheme_id", drop=False), how="left", rsuffix="_sch"
    )\
    .set_index("intermediate_id_sch", drop=False).join(
        intermediates_df.set_index("intermediate_id", drop=False), how="left", rsuffix="_intr"
    )\
    .set_index("stage_reagent_cond_id", drop=False).join(
        src_df.set_index("stage_reagent_cond_id", drop=False), how="left", rsuffix="_src"
    )\
    .set_index("compound_id_intr", drop=False).join(
        compounds_df.set_index("compound_id", drop=False), how="left", rsuffix="_interm_c"
    )
    
    
    df.drop([i for i in df.columns if i not in COL_ORDER], axis=1, inplace=True)
    df.rename(columns=COLUMNS, inplace=True)
    df[list(COLUMNS.values())].to_excel(f"result_{datetime.now().__str__()}.xlsx")


if __name__ == "__main__":
    main()
