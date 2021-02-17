# run.py
# python routine for running the script
import sys
import pandas as pd
from append_vid_info import append_vid_info
from scrape_from_df import scrape_from_df

if __name__ == '__main__':
    filename = 'test.ods'
    output = 'test-output.ods'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        output = 'vidinfo-' + filename
    df = pd.read_excel(filename)
    inf = scrape_from_df(df)
    append_vid_info(inf, df)
    df.to_excel(output, index=False)
