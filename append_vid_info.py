# append_vid_info.py
# python script appending vid info to a given dataframe
import numpy as np
import pandas as pd
from scrape_from_df import scrape_from_df


def append_vid_info(vidinfo, dataframe):
    title = np.array([], dtype=str)
    channelid = np.array([], dtype=str)
    likecount = np.array([], dtype=str)
    dislikecount = np.array([], dtype=str)
    commentcount = np.array([], dtype=str)
    duration = np.array([], dtype=str)

    for item in vidinfo:
        title = np.append(title, item['title'])
        channelid = np.append(channelid, item['channelId'])
        likecount = np.append(likecount, item['likeCount'])
        dislikecount = np.append(dislikecount, item['dislikeCount'])
        commentcount = np.append(commentcount, item['commentCount'])
        duration = np.append(duration, item['duration'])

    name = gcn(channelid)

    dataframe['title'] = title
    dataframe['ChannelName'] = name
    dataframe['channelId'] = channelid
    dataframe['likeCount'] = likecount
    dataframe['dislikeCount'] = dislikecount
    dataframe['commentCount'] = commentcount
    dataframe['duration'] = duration

    return dataframe


if __name__ == '__main__':
    filename = 'test.ods'
    output = 'test-output.ods'
    df = pd.read_excel(filename)
    inf = scrape_from_df(df)
    append_vid_info(inf, df)

    df.to_excel(output, index=False)
