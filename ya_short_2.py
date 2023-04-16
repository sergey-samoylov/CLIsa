import httpx
from selectolax.parser import HTMLParser

def question2alisa(query):
    user_query = query
    y_query = user_query.split(" ")
    x_query = "%20".join(y_query)
    url = 'https://ya.ru/search/?text=' + x_query

    resp = httpx.get(
        url,
        headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
        },
    )

    html = HTMLParser(resp.text)

    lst1 = [node.text() for node in html.css('.Fact-ECFragment')]
    if len(lst1) > 0:
        res = ' '.join([str(x) for x in lst1])
        return res
    lst2 = [node.text() for node in html.css('.Fact-Answer')]
    if len(lst2) > 0:
        res = ' '.join([str(x) for x in lst2])
        return res
    lst3 = [node.text() for node in html.css('.Translate-ValuesContent')]
    if len(lst3) > 0:
        res = ' '.join([str(x) for x in lst3])
        return res

    # lst = lst1 if len(lst1) > 0 else lst2

    # return print(*lst)
