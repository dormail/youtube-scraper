# append_vid_info.py
# python script appending vid info to a given dataframe

import numpy as np
from youtube_utils import get_channel_name
from youtube_utils import get_channel_data as gcd

gcn = np.vectorize(get_channel_name)
#gcd = np.vectorize(get_channel_data)

def append_vid_info(vidinfo, dataframe):
    title = np.array([], dtype=str)
    channelid = np.array([], dtype=str)
    likecount = np.array([], dtype=str)
    dislikecount = np.array([], dtype=str)
    commentcount = np.array([], dtype=str)
    duration = np.array([], dtype=str)

    # channel related arrays
    channelName = np.array([], dtype=str)
    channelSubs = np.array([], dtype=str)

    try:
        for item in vidinfo:
            title = np.append(title, item['title'])
            channelid = np.append(channelid, item['channelId'])
            likecount = np.append(likecount, item['likeCount'])
            dislikecount = np.append(dislikecount, item['dislikeCount'])
            commentcount = np.append(commentcount, item['commentCount'])
            duration = np.append(duration, item['duration'])

            channelData = gcd(item['channelId'])
            channelName = np.append(channelName, channelData['channelName'])
            channelSubs = np.append(channelSubs, channelData['subscriberCount'])
            
    
    except TypeError:
        print('Ooops, something went wrong during scraping')

    dataframe['channelId'] = channelid
    dataframe['ChannelName'] = channelName
    dataframe['ChannelSubs'] = channelSubs

    dataframe['title'] = title
    dataframe['likeCount'] = likecount
    dataframe['dislikeCount'] = dislikecount
    dataframe['commentCount'] = commentcount
    dataframe['duration'] = duration

    return dataframe
