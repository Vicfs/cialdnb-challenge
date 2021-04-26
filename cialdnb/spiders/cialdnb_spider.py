import scrapy
import string

from cialdnb.utils import find_phone_number, phone_cleanup

class LogosNumbersSpider(scrapy.Spider):
    name = "LogosNumbers"
    handle_httpstatus_list = [403, 404] # Allow 403 and 404 responses

    def __init__(self, urls, **kwargs):
        self.urls = urls

        super().__init__(**kwargs)

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(
                url=url, callback=self.parse
            )

    def parse(self, response):
        self.logger.warning(f"{response.status} response from: {response.url}")
        html_text = response.text
        phone_numbers = find_phone_number(html_text)
        phone_numbers = phone_cleanup(phone_numbers)
        # Get the url name including "https://"
        page_name = f"{response.url.split('/')[0]}//{response.url.split('/')[2]}"
        # Make search for logo case insensitive, had to ignore pep8
        contains_logosrc = "contains(translate(@src, 'ABCDEFGHIJKLMNOPQRSTUVXWYZ', 'abcdefghijklmnopqrstuvxwyz'), 'logo')"
        contains_logoclass = "contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVXWYZ', 'abcdefghijklmnopqrstuvxwyz'), 'logo')"
        logo_url = response.xpath(
            f"//img[{contains_logosrc} or {contains_logoclass}]/@src"
        ).get(default="")
        # If page wasn't included in logo url, include it
        if logo_url and logo_url.startswith("/") or "http" not in logo_url:
            logo_url = page_name + logo_url.replace("//", "/")
        yield {
            "logo": logo_url,
            "phone numbers": phone_numbers,
            "website": response.url,
        }
