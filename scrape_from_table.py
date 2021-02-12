# scrape_from_table.py
# scrape_from_table gets receives a dataframe and scrapes 
# the youtube vid info for every link in the 'link' column

from get_video_data import get_video_data as gvd

def scrape_from_table(df):
    links = df['link']

    return df


# module test
if __name__ == '__main__':

