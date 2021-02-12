# links_to_id.py

def links_to_id(link):
    vid_id = link.split('watch?v=')[1]
    return vid_id

if __name__ == '__main__':
    print(links_to_id('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
