# youtube_utils.py

import requests
import csv
import json

from secret import key

API_KEY = key

def get_video_data(vid_id):
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


if __name__ == '__main__':
    vid_id = 'sehyLDPeB6M'
    name = get_video_data(vid_id)
    print(name)
