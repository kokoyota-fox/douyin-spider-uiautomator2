from App import Douyin
import asyncio
import pandas as pd
import os

if __name__ == '__main__':
    assert os.path.exists('config.csv')
    data = pd.read_csv('config.csv')
    task = []
    for _, row in data.iterrows():
        model = row['model']
        douyin = Douyin(row)
        if model == 'z':
            task.append(douyin.random_direct_broadcasting_room_scribe())
        if model == 's':
            task.append(douyin.fans_list_scribe_and_personal_letter())
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*task))
