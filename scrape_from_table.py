# scrape_from_table.py
# scrape_from_table gets receives a dataframe and scrapes 
# the youtube vid info for every link in the 'link' column
# returns a list with a dict for every video given in the df

from get_video_data import get_video_data
from links_to_id import links_to_id
import pandas as pd
import numpy as np

gvd = np.vectorize(get_video_data)
ldi = np.vectorize(links_to_id)

def scrape_from_table(df):
    links = df['link']
    vid_id = ldi(links)
    vid_info = gvd(vid_id)

    return vid_info


# module test
if __name__ == '__main__':
    filename = 'test.ods'
    df = pd.read_excel(filename)
    info = scrape_from_table(df)
    print(info)
