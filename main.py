import logging
import sys

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from cialdnb.spiders.cialdnb_spider import LogosNumbersSpider


def main():
    # Start scrapy process
    process = CrawlerProcess(get_project_settings())

    logger = logging.getLogger(__name__)

    # Check for stdin input
    if sys.stdin.isatty():
        logger.error("input must be passed via stdin!")
        sys.exit(1)

    # Get urls from stdin
    urls = sys.stdin.read().splitlines()
    logger.warning(f"urls received as input: {urls}")

    process.crawl(LogosNumbersSpider, urls=urls)
    process.start()

if __name__ == "__main__":
    main()
