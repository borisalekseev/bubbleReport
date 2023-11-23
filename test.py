from file_readers import CompoundsReader, IntermediatesReader, SchemeCartReader, SchemeCartCondReader, SchemesReader, StageReagentCondReader, StagesReader


print(CompoundsReader().get_df().head())
print(IntermediatesReader().get_df().head())
print(SchemeCartReader().get_df().head())
print(SchemeCartCondReader().get_df().head())
print(SchemesReader().get_df().head())
print(StageReagentCondReader().get_df().head())
# print(StagesReader().get_df().head())