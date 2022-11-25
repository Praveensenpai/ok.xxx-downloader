
# OK.XXX Downloader

Download from ok.XXX



## How to

#### First install requirements

```http
  pip install -r requirements.txt
```



## Usage/Examples

#### Example 1 - Download lots of videos from page
```python
page_url = "https://ok.xxx/models/susy-gala/"
okxxx = OkXXXDownloader()
okxxx.download(page_url, page=True, parallel_download=12)

```

#### Example 2 - Download a single video
```python
okxxx = OkXXXDownloader()
okxxx.download(url="https://ok.xxx/video/103650/")

```
