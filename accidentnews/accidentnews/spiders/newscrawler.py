# pip install win32api scrapy html2text

import scrapy
import html2text
import csv, re
import nltk

nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')

class NewsCrawler(scrapy.Spider):
    name = "newscrawler"

    def getloc(sentence):
        result = []
        for sent in nltk.sent_tokenize(sentence):
            print(type(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent)))))
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                # print(chunk)
                if hasattr(chunk, 'label'):
                    if chunk.label() == "GPE":
                        result.append(' '.join(c[0] for c in chunk))
        return result

    def start_requests(self):
        urls = [
            'https://timesofindia.indiatimes.com/topic/accident-prone-areas',
            'https://timesofindia.indiatimes.com/topic/accident-prone-areas/2',
            'https://timesofindia.indiatimes.com/topic/accident-prone-areas/3',
            'https://timesofindia.indiatimes.com/topic/accident-prone-areas/4'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if re.match(".*/topic/.*", response.url):
            domain = "/".join(response.url.split("/")[:3])
            a = response.css('ul[itemprop="ItemList"] a::attr(href)').extract()
            for i in a:
                if i[0] == '/':
                    i = domain + i
                yield scrapy.Request(url=i, callback=self.parse_news)

    def parse_news(self, response):
        main = response.css('div.main-content')
        title = main.css('section.title_section arttitle::text').get()
        time = main.css('section.title_section span.time_cptn time::attr(datetime)').get()

        h = html2text.HTML2Text()
        h.ignore_links = True
        content = h.handle(response.css('div.article_content arttextxml').get()).replace("**", "").replace("\n", " ")

        # with open('news.csv', 'a') as csvFile:
        #    writer = csv.writer(csvFile,lineterminator='\n')
        #    writer.writerow([title, time, content])

        yield {'lat':getlat(title, content),'long':getlong(title, content),'title': title, 'time': time, 'content': content}
