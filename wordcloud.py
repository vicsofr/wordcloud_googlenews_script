import feedparser
from collections import Counter
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wc_from_google_news(word: str, days: str):
    # Grabbing news from GoogleNews for last N-days with some English
    # word and showing a WordCloud image with 50 most popular words
    # in the articles.
    url = f'https://news.google.com/rss/search?q={word}%20when%3A{days}d&hl=cc'
    f'en-US&gl=US&ceid=US%3Aen'
    news = []
    feed = feedparser.parse(url)
    for post in feed.entries:
        a = post.title.split(' - ')
        a.remove(a[-1])
        news.append(''.join(a))

    cnt = Counter(x for x in re.findall(r'[A-z\']{4,}', ''.join(news)))
    top50 = []
    for i in cnt.most_common(50):
        top50.append(i[0])

    wordcloud = WordCloud(background_color='white', width=1200,
                          height=1000).\
        generate_from_frequencies(dict(cnt.most_common(50)))

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


wc_from_google_news(str(input('Type some English word you want to find from'
                              'Google News articles: ')),
                    str(input('Type the number of days for which you want to'
                              'find news: ')))