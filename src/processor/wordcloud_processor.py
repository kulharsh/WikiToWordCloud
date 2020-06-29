import re
import pandas as pd
from wordcloud import WordCloud, STOPWORDS 

def get_text_from_df(df, word):
    text = ""
    regex = re.compile('[^a-zA-Z1-9_\- ]')
    removeWords = [word, "birth_place", "death_place", "wikipedia"]
    for val in df.abstract: 

        # typecaste each val to string 
        val = str(val) 
        val = regex.sub(" ", val)
        # split the value 
        tokens = val.split() 

        # Converts each token into lowercase 
        for i in range(len(tokens)):
            lowered = tokens[i].lower()
            if lowered not in removeWords and len(lowered)>2:
                tokens[i] = lowered 
            else:
                tokens[i] = ""

        text += " ".join(tokens)+" "
        
    for val in df.title: 

        # typecaste each val to string 
        val = str(val) 
        val = regex.sub(" ", val)
        # split the value 
        tokens = val.split() 

        # Converts each token into lowercase 
        for i in range(len(tokens)):
            lowered = tokens[i].lower()
            if lowered not in removeWords:
                tokens[i] = lowered 
            else:
                tokens[i] = ""

        text += " ".join(tokens)+" "
    return text

def get_search_results(es, word):
    resp = es.search(index = "temp1", body={"query": {"match": {'abstract':word}}}, scroll = "10m", size = 100, request_timeout = 300)
    resps = []
    while len(resp['hits']['hits']) > 0 and len(resps) < 100000: 
        for h in resp['hits']['hits']:
            resps.append(h['_source'])
        resp = es.scroll(scroll_id=resp['_scroll_id'], scroll = "10m")
    df = pd.DataFrame(resps)
    return df


def get_wordCloud(es, word, path):
    df = get_search_results(es, word)
    text = get_text_from_df(df, word)
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = set(list(STOPWORDS)), 
                min_font_size = 10).generate(text) 
  
    # plot the WordCloud image                        
    wordcloud.to_file(path)
