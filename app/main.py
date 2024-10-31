from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
import feedparser
from feedgen.feed import FeedGenerator
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/medium_rss")
async def medium_rss(tags: str):
    tag_list = tags.split(',')
    fg = FeedGenerator()
    fg.title("Medium Aggregated Feed")
    fg.link(href="https://medium.com", rel="alternate")
    fg.description("Aggregated RSS feed of selected Medium topics.")
    fg.language("en")

    for tag in tag_list:
        url = f"https://medium.com/feed/tag/{tag}"
        feed = feedparser.parse(url)
        for entry in feed.entries:
            fe = fg.add_entry()
            fe.id(entry.id)
            fe.title(entry.title)
            fe.link(href=entry.link)
            fe.description(entry.summary)
            fe.published(entry.published if hasattr(entry, 'published') else datetime.now().isoformat())

    rss_feed = fg.rss_str(pretty=True)
    return Response(rss_feed, media_type='application/rss+xml')
