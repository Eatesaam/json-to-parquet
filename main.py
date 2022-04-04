import json
import pyarrow.parquet as pq
from pyarrow import json as pa
import pandas as pd

jsonFile = "file.json"

getfileName = str(jsonFile)
splitFileName = getfileName.split(".")
fileName = splitFileName[0]

parquetFile = fileName+".parquet"

table = pa.read_json(jsonFile) 
pq.write_table(table, parquetFile)

# df = pd.read_json(jsonFile)

# df.to_parquet(parquetFile)