import pandas as pd
import os
from sqlalchemy import create_engine
import logging

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine("sqlite:///inventory.db")

def ingest_db(df, table_name, engine, first_chunk):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, 
              con = engine, 
              if_exists='replace' if first_chunk else 'append', 
              index=False, 
              chunksize=10_000)


def load_raw_data():
    '''this function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            table_name = file[:-4]
            first_chunk= True
            total=0

            for chunk in pd.read_csv("data/"+file, chunksize=200_000):
                logging.info(f'Ingesting {file} in db')
                ingest_db(chunk, table_name, engine, first_chunk)
                first_chunk = False
                total += len(chunk)
                print(f"{table_name}: {total} rows loaded")
                
    end = time.time()
    total_time= (end - start)/60
    
    logging.info("---------Ingestion Complete-----------")
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()