from scraper import CategoryScraper

def main():
    scraper = CategoryScraper("https://www.homestratosphere.com/furniture/")
    scraper.scrape()


if __name__ == "__main__":
    main()