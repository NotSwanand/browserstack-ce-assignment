from driver.driver_setup import setup_driver
from scraper.link_collector import get_article_links
from scraper.article_scraper import scrape_article
from utils.translator import translate_titles
from utils.word_analysis import find_repeated_words


def main():

    print("\n=== NEW BROWSER SESSION STARTED ===\n")

    driver = setup_driver()

    links = get_article_links(driver)

    titles = []
    count = 0

    for link in links:

        title, content = scrape_article(driver, link, count)

        if title and content:

            print("SPANISH TITLE:", title)
            print(content[:300])

            titles.append(title)
            count += 1

        if count == 5:
            break

    translated = translate_titles(titles)

    print("\nTRANSLATED TITLES:")

    for t in translated:
        print(t)

    print("\nREPEATED WORDS:")
    find_repeated_words(translated)

    driver.quit()


if __name__ == "__main__":
    main()