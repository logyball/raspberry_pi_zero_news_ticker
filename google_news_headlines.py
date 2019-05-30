# get the top 3 headlines split up by state and national news

import feedparser, ssl

STATE = 'Oregon'
ssl._create_default_https_context=ssl._create_unverified_context


def get_stories(url):
    parsed_rss = feedparser.parse(url)
    title_source_list = []
    for story in parsed_rss['entries']:
        title_source = story['title'].rsplit('-', 1)
        title_source_list.append((title_source[0].rstrip(), title_source[1].lstrip()))
        if len(title_source_list) > 2:
            break
    return title_source_list


def get_national():
    url = 'https://news.google.com/rss'
    return get_stories(url)
    

def get_local():
    url = f'https://news.google.com/news/rss/headlines/section/geo/{STATE}'
    return get_stories(url)