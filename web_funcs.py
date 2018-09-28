#import libraries
from contextlib import closing
from requests import get
from requests.exceptions import RequestException

#---------------------------------------------------------------------
#webscrape functions:
#web request func
def get_url(url):
    #makes HTTP Get request
    #if content type HTML/XML, return the text content
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error("Error during requests to {0} : {1}".format(url, str(e)))
        return None

def is_good_response(resp):
    #if response is HTMl, return true, else False
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    print(e) #prints error message