# links_to_id.py

def links_to_id(link):
    try:
        vid_id = link.split('watch?v=')[1]
    except IndexError:
        print('IndexError: ' + str(link) + ' could not be parsed.')
        return -1
    except AttributeError:
        print('AttributeError: ' + str(link) + ' could not be parsed.')
        return -1
    return vid_id
