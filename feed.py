import feedparser 

def parser(url):
	return feedparser.parse(url)

def get_source(parsed):
	feed = parsed['feed']
	return{
		'link': feed['Link']
		'title': feed['title']
		'subtitle': feed['subtitle']

	}

def get_articles(parsed):
	articles = []
	entries = parsed['entries']
	for entry in entries:
		articles.append({
			'id': entry['id'],
			'link': entry['link'],
			'title': entry['title'],
			'summary': entry['summary'],
			'published': entry['published_parsed'],


			})
	return articles