# scrape_from_table.py
# scrape_from_table gets receives a dataframe and scrapes 
# the youtube vid info for every link in the 'link' column

from get_video_data import get_video_data
import pandas as pd
import numpy as np

gvd = np.vectorize(get_video_data)

def scrape_from_table(df):
    links = df['link']
    vid_id = split('watch?v=', links)
    vid_info = gvd(links)

    return vid_info


# module test
if __name__ == '__main__':
    filename = 'test.xlsx'
    df = pd.read_excel(filename)

    links = scrape_from_table(df)
    print(links)
