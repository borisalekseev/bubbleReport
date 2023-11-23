from abc import ABC
import pandas as pd
from pydantic import TypeAdapter
import os
import settings
import re


class ReaderBase(ABC):
    list_parser: TypeAdapter
    pattern: str

    def get_df(self) -> pd.DataFrame:
        with open(self.file_path, "rb") as f:
            data = self.list_parser.validate_json(f.read())
        df = pd.DataFrame([d.dict() for d in data])
        df.rename(columns=self.rename_columns, inplace=True)
        return df

    @property
    def file_path(self) -> str:
        if self.file_name is None:
            raise ValueError(f"Cannot find file for {self.__class__.__name__}")
        return os.path.join(settings.FILES_PATH, self.file_name)

    @property
    def file_name(self) -> str:
        name =  next(
            (name for name in os.listdir(settings.FILES_PATH) if re.match(self.pattern, name)), None
        )
        return name

    @property
    def rename_columns(self) -> dict[str, str]:
        return {}
