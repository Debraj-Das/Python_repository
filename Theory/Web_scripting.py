from bs4 import BeautifulSoup

with open("index.html") as fp:
    contain = fp.read()
    # print(contain)
    soup = BeautifulSoup(contain, 'lxml')
    # print(soup.prettify())
    h2 = soup.find_all('p')
    print(h2)
