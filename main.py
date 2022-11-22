from selectolax.parser import HTMLParser
import requests
import wget

DOWNLOAD_PATH = "downloads"
PAGE_URL = "https://ok.xxx/models/susy-gala/"


def souper(url: str) -> HTMLParser:
    r = requests.get(url)
    return HTMLParser(r.text)


def get_download_link(url: str) -> str:
    # need to fix this / add this
    soup = souper(url)
    return soup.css("a[class='download-link']")[-1].attributes["href"]


def downloader(link: str) -> None:
    wget.download(url=link)


def page_viewer(page_url: str) -> list:
    soup = souper(page_url)
    return [
        f'https://ok.xxx{i.attributes["href"]}'
        for i in soup.css(".thumb.thumb-video a")
    ]


if __name__ == "__main__":
    video_page_links = page_viewer(PAGE_URL)
    for video_page in video_page_links:
        link = get_download_link(video_page)
        downloader(link)
