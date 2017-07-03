import urllib.request
class Html_Downloader():
    def download(self,url):
        if url is None:
            return
        header={'User-Agent':'Mozilla/5.0'}
        resp=urllib.request.urlopen(url)
        if resp.getcode()!=200:
            return
        return  resp.read().decode('utf-8')  #关键
