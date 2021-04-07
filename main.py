from App import Douyin
import asyncio
import pandas as pd
import os

if __name__ == '__main__':
    assert os.path.exists('config.csv')
    data = pd.read_csv('config.csv')
    task = []
    for _, row in data.iterrows():
        douyin = Douyin(row)
        task.append(douyin.personal_letter())
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*task))
