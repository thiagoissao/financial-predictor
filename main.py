# 1. consultar uma api para extrair noticias financeiras
# 2. aplicar modelos de PLN em cada noticia
# 3. aplicar análise de sentimento e classificar as noticias em uma escala
# 4. coletar os preços de fechamento da ação e informar a variação do preço de um dia para o outro
# 5. fazer a análise de correlação entre os sentimentos das notícias e a variação de preço
import re
from lxml import html
import requests

HOME_PAGE = 'https://br.investing.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Utiliza o site investing para extrar a página referente à magazine luiza
homepageUrl = '{HOME_PAGE}/equities/magaz-luiza-on-nm'.format(
    HOME_PAGE=HOME_PAGE)

# URL que faz referências para o site br.investing.com
news = '/news'


def filterLinks(substring, links):
    newLinks = []
    for link in links:
        if(link.find(substring) == 0):
            newLinks.append(link)
    return newLinks


def getPageContent(link):
    page = requests.get(link, headers=headers)
    tree = html.fromstring(page.content)
    titles = tree.xpath('//h1[@class="articleHeader"]/text()')
    paragraphs = tree.xpath('//div[@class="WYSIWYG articlePage"]//p/text()')
    return (titles, paragraphs)


# Faz a requisição do html da página
page = requests.get(homepageUrl)
tree = html.fromstring(page.content)

htmlNewsLinks = tree.xpath(
    '//div[@data-test="news-container"]//a/@href')

newsLinks = filterLinks(news, htmlNewsLinks)

# coleta o título e as tags p de cada link de notícias
print('NOTÍCIAS')
for link in newsLinks:
    titles, paragraphs = getPageContent(HOME_PAGE + link)

    # construir uma análise de sentimentos aqui
    print(titles)
    print(paragraphs)
