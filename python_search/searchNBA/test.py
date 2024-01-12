from bs4 import BeautifulSoup as bs

# 原始 HTML 程式碼 假設我們已經有檔案了
html_doc = """
<html><head><title>前進吧！高捷少女</title></head>
<body><h2>K.R.T. GIRLS</h2>
<p>小穹</p>
<p>艾米莉亞</p>
<p>婕兒</p>
<p>耐耐</p>
<a id="link1" href="https://zh.wikipedia.org/wiki/%E9%AB%98%E6%8D%B7%E5%B0%91%E5%A5%B3#%E5%B0%8F%E7%A9%B9">Link 1</a>
<a id="link2" href="https://zh.wikipedia.org/wiki/%E9%AB%98%E6%8D%B7%E5%B0%91%E5%A5%B3#%E8%89%BE%E7%B1%B3%E8%8E%89%E4%BA%9E">Link 2</a>
<a id="link3" href="https://zh.wikipedia.org/wiki/%E9%AB%98%E6%8D%B7%E5%B0%91%E5%A5%B3#%E5%A9%95%E5%85%92 3</a>
<a id="link4" href="https://zh.wikipedia.org/wiki/%E9%AB%98%E6%8D%B7%E5%B0%91%E5%A5%B3#%E8%80%90%E8%80%90">Link 4</a>
</body></html>
"""

soup = bs(html_doc, 'html.parser')
web_title=soup.title

print(web_title)
