from selectolax.parser import HTMLParser
import requests
import wget
from concurrent.futures import ThreadPoolExecutor


class OkXXXDownloader:
    def download(self, url: str, page: bool = False, parallel_download: int = 10):
        if not page:
            self._downloader(self._get_download_link(url))
        else:
            video_page_links = self._page_viewer(url)
            print(f"Total Pages = {len(video_page_links)}")
            with ThreadPoolExecutor(max_workers=len(video_page_links)) as executor:
                links = executor.map(self._get_download_link, video_page_links)
                dlinks = [i for i in links]
            print(f"PARALLEL DOWNLOAD = {parallel_download}")
            with ThreadPoolExecutor(max_workers=parallel_download) as executor:
                executor.map(self._downloader, dlinks)

    def _souper(self, url: str) -> HTMLParser:
        r = requests.get(url)
        return HTMLParser(r.text)

    def _get_download_link(self, url: str) -> str:
        print(f">>> {url}")
        soup = self._souper(url)
        return soup.css("a[class='download-link']")[-1].attributes["href"]

    def _custom_bar(self, current, total, width=80):
        return wget.bar_adaptive(round(current/1024/1024, 2), round(total/1024/1024, 2), width) + ' MB'

    def _downloader(self, link: str) -> None:
        wget.download(url=link, bar=self._custom_bar)

    def _page_viewer(self, page_url: str) -> list:
        soup = self._souper(page_url)
        return [
            f'https://ok.xxx{i.attributes["href"]}'
            for i in soup.css(".thumb.thumb-video a")
        ]
