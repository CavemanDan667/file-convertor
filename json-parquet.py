# pip install pandas pyarrow

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os


def json_to_parquet(json_file):
    json_name = os.path.splitext(json_file)[0]
    data = open(json_file, "r")
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f'{json_name}.parquet')
