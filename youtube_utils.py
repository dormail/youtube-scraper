# youtube_utils.py
# get_video_data  returns a dict with data about a youtube video for a given video id

import requests
import json
from secret import key as API_KEY


def get_video_data(vid_id):
    if vid_id == '-1':
        data = {
            'title': '',
            'channelId': '',
            'likeCount': '',
            'dislikeCount': '',
            'commentCount': '',
            'duration': '',
        }
        return data

    # api parameters
    params = 'snippet,status,contentDetails,statistics,topicDetails,localizations'
    api_url = 'https://www.googleapis.com/youtube/v3/videos?part='+ params +'&id='+ vid_id+'&key='+API_KEY

    # this opens the link and tells your computer that the format it is reading is JSON
    api_response = requests.get(api_url)
    videodetails = json.loads(api_response.text)
    if len(videodetails['items']) > 0:
        item = videodetails['items'][0]
        snippet = item.get('snippet', {})
        title = snippet.get('localized', {}).get('title', {})
        channelId = snippet.get('channelId', {})

        stats = item.get('statistics', {})
        likeCount = stats.get('likeCount', {})
        dislikeCount = stats.get('dislikeCount', {})
        commentCount = stats.get('commentCount', {})

        duration = item.get('contentDetails', {}).get('duration', {})[2:]

        data = {
                'title': title,
                'channelId' : channelId,
                'likeCount': likeCount,
                'dislikeCount': dislikeCount,
                'commentCount': commentCount,
                'duration': duration,
        }

        return data
    else:
        print(vid_id + ' is an invalid video id')


def get_channel_name(channelid):
    if channelid == '':
        print(channelid + ' is an invalid channel id.')
        return ''
    params = 'snippet%2CcontentDetails%2Cstatistics'
    api_url = 'https://youtube.googleapis.com/youtube/v3/channels?part=' + params + '&id=' + channelid + '&key=' + API_KEY
    api_response = requests.get(api_url)
    videodetails = json.loads(api_response.text)
    if len(videodetails['items']) > 0:
        item = videodetails['items'][0]
        name = item['snippet']['title']
        return name
    else:
        print(channelid + ' is not a valid youtube channel id.')
        return -1


if __name__ == '__main__':
    vid_id = 'sehyLDPeB6M'
    channelid = get_video_data(vid_id)['channelId']
    name = get_channel_name(channelid)
    print(name)
