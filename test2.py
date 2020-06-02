from aiorss import rssparser

def test(feed):
    f = rssparser(feed)
    return f.entries