import time
import requests
from bs4 import BeautifulSoup


def url_of_first_page(url):
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    head = soup.head
    url_link = head.find('link', rel='canonical')['href']
    print(url_link)
    request(url_link)


def request(url):
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    title = soup.find('h1').contents[0]
    print(title)
    if title == "Philosophy":
        return
    next_page = get_first_link(soup)
    if next_page:
        first_link = "https://en.wikipedia.org" + next_page
        time.sleep(0.5)
        request(first_link)


def get_first_link(soup):
    content = soup.find(id="content")
    body_content = content.find(id="bodyContent")
    mw_content_text = body_content.find(id="mw-content-text")
    mw_parser_content = mw_content_text.find("div", {"class": "mw-parser-output"})
    target = mw_parser_content.find_all('p')
    for paragraph in target:
        paragraph = BeautifulSoup(remove_brackets(paragraph), 'html.parser')
        a = paragraph.find_all('a', href=True)
        for link in a:
            if check_if_italic(str(link.find_previous())):
                continue
            plain = link['href']
            if plain[:6] == "/wiki/":   # Only find links that redirects to other Wikipedia pages
                return plain            # Escaping "RED LINKS"


def remove_brackets(string):
    """
    remove brackets from a string
    leave brackets between "<a></a>" tags in place
    hihi, this is like an automata
    """
    string = "" + str(string)
    # print "input: ",string
    d = 0
    k = 0
    out = ''
    for i in string:
        # check for tag when not in parantheses mode
        if d < 1:
            if i == '>':
                k -= 1

            if i == "<":
                k += 1

        # check for parentheses
        if k < 1:
            if i == '(':
                d += 1

            if d > 0:
                out += ' '
            else:
                out += i

            if i == ')':
                d -= 1
        else:
            out += i

    # print "output: ",out
    return out


def check_if_italic(string):
    if string[1]== "i":
        return True


random_url = 'https://en.wikipedia.org/wiki/Special:Random'
url_of_first_page(random_url)
test1 = 'https://en.wikipedia.org/wiki/War_Powers_Clause'
#url_of_first_page(test)
