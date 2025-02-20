import pandas as pd
import os

from pathlib import Path
from datamodel_b07_tc.core.metadata import Metadata


class GstaticParser:
    def __init__(
        self,
        path_to_directory: str | bytes | os.PathLike | Path,
        file_suffix: str,
    ):
        """Pass the path to a directory containing CSV-type files of the GC to be
        read.

        Args:
            path_to_directory (str | bytes | os.PathLike): Path to a directory containing CSV-type files.
        """
        file_search_pattern = "*." + file_suffix
        path_list = list(Path(path_to_directory).glob(file_search_pattern))
        self._available_files = {
            count: file
            for count, file in enumerate(path_list)
            if file.is_file()
        }

    def __repr__(self):
        return "Gstatic parser"

    def extract_metadata(self, file_index: int) -> dict:  # filestem: str
        metadata_df = pd.read_csv(
            self._available_files[file_index],
            sep="\t",
            names=[
                "Parameter",
                "Data_type",
                "Value",
                "Description",
            ],
            engine="python",
            encoding="utf-8",
            skiprows=[
                *[i for i in range(0, 7)],
                *[j for j in range(55, 3658)],
            ],
        )
        metadata_list = []
        for index in metadata_df.index:
            metadata_list.append(
                Metadata(
                    parameter=metadata_df["Parameter"][index],
                    data_type=metadata_df["Data_type"][index],
                    value=metadata_df["Value"][index],
                    description=metadata_df["Description"][index],
                )
            )
        return metadata_df, metadata_list

    @property
    def available_files(self) -> list[str]:
        return self._available_files
        # for line in open(self.file, 'r'):
        #     line = line.strip()
        #     if '=' in line:
        #         key_value = re.split('=', line.strip(r'_'))
        #         try:
        #             self.meta_data[key_value[0]] = float(key_value[1].strip("'"))
        #         except ValueError:
        #             self.meta_data[key_value[0]] = key_value[1].strip("'")
        # meta_data = self.meta_data
        # self.convert_datetime(meta_data)
        # self.rename_2theta(meta_data)
        # self.concatinate_wls(meta_data)
        # return meta_data

    # def convert_datetime(self, meta_data):
    #     datemeasured = meta_data["DATEMEASURED"]
    #     pattern_date = r"([0-9]{1,2})\-([A-Za-z]*)\-([0-9]{4})\s([0-9]{2})\:([0-9]{2})\:([0-9]{2})"
    #     months = [
    #         "jan",
    #         "feb",
    #         "mar",
    #         "apr",
    #         "may",
    #         "jun",
    #         "jul",
    #         "aug",
    #         "sep",
    #         "oct",
    #         "nov",
    #         "dec",
    #     ]
    #     date_raw = re.findall(pattern_date, datemeasured)[0]
    #     datum = []
    #     for part in date_raw:
    #         try:
    #             datum.append(int(part))
    #         except ValueError:
    #             datum.append(months.index(part.lower()) + 1)
    #     date = datetime(
    #         datum[2], datum[1], datum[0], datum[3], datum[4], datum[5]
    #     )
    #     meta_data["DATEMEASURED"] = date

    # def enumerate_available_files(self) -> dict[int, str]:
    #     """Enumerate the CSV files available in the given directory and
    #     return a dictionary with their index and name.

    #     Returns:
    #         dict[int, str]: Indices and names of available files.
    #     """
    #     return {
    #         count: value for count, value in enumerate(self.available_files)
    #     }
