# Date: Feb 20, 2021

from pathlib import Path
import os
import json
import pandas as pd
import PupilFolderFileCheck as flchk

RECORDING = flchk.ask_location()
os.chdir(RECORDING)

pd.options.display.float_format = '{:}'.format
DATAFRAME_HEAD_COUNT = 3  # gets information from 3 rows.

with Path(RECORDING).joinpath('info.player.json').open() as file:
    meta_file = json.load(file)
print(meta_file)


start_timestamp_unix = meta_file["start_time_system_s"]
start_timestamp_pupil = meta_file["start_time_synced_s"]
start_timestamp_diff = start_timestamp_unix - start_timestamp_pupil


def convert_and_save_timestamps(input_path, column_names, timestamp_offset=start_timestamp_diff):

    """ This function takes path where the file is and column names that need to be transformed as input. The output
        is the transformed file that is renamed using the stem and suffix of the file within the input directory. """

    output_path = input_path.with_name(input_path.stem + "_unix_datetime").with_suffix(input_path.suffix)
    df = pd.read_csv(input_path)
    for column_name in column_names:
        unix_column_name = column_name + "_unix"
        datetime_column_name = column_name + "_datetime"
        df[unix_column_name] = df[column_name] + timestamp_offset
        df[datetime_column_name] = pd.to_datetime(df[unix_column_name], unit="s")
    df.to_csv(output_path)
    return df.head(DATAFRAME_HEAD_COUNT)


if __name__=="__main__":
# Surface Files:
    convert_and_save_timestamps(input_path=Path(RECORDING).joinpath("surfaces/surface_events.csv"),
                                column_names=["world_timestamp"])

    convert_and_save_timestamps(input_path=Path(RECORDING).joinpath("surfaces/fixations_on_surface_Cleo.csv"),
                                column_names=["world_timestamp", "start_timestamp"])

    convert_and_save_timestamps(input_path=Path(RECORDING).joinpath("surfaces/surf_positions_Cleo.csv"),
                                column_names=["world_timestamp"])

    convert_and_save_timestamps(input_path=Path(RECORDING).joinpath("surfaces/gaze_positions_on_surface_Cleo.csv"),
                                column_names=["world_timestamp", "gaze_timestamp"])

    convert_and_save_timestamps(input_path=Path(RECORDING).joinpath("surfaces/surf_positions_Cleo.csv"),
                                column_names=["world_timestamp"])

    # General Files:

    convert_and_save_timestamps(input_path=Path(RECORDING).joinpath("fixations.csv"),
                                column_names=["start_timestamp"])

    convert_and_save_timestamps(input_path=Path(RECORDING).joinpath("gaze_positions.csv"),
                                column_names=["gaze_timestamp"])

    convert_and_save_timestamps(input_path=Path(RECORDING).joinpath("pupil_positions.csv"),
                                column_names=["pupil_timestamp"])
