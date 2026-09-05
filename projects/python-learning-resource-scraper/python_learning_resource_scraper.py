import threading

import requests
from bs4 import BeautifulSoup


GLOBAL_VERSION = "Resource Scraper v1.0"


def scrape_resource(url, verbose=False):
    local_info = "Scraping Python learning resource"

    def show_info():
        print("Info:", local_info)
        print("Version:", GLOBAL_VERSION)

    if verbose:
        show_info()

    try:
        response = requests.get(url, timeout=10)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "html.parser")

        extract_title = lambda soup_obj: (
            soup_obj.title.string if soup_obj.title and soup_obj.title.string
            else "No Title Found"
        )
        page_title = extract_title(soup).strip()

        heading_tag = soup.find("h1")
        if heading_tag:
            section_number = heading_tag.find("span", class_="section-number")
            if section_number:
                section_number.decompose()

            permalink = heading_tag.find("a", class_="headerlink")
            if permalink:
                permalink.decompose()

        main_heading = (
            heading_tag.get_text(strip=True)
            if heading_tag
            else "No H1 Heading Found"
        )

        return {
            "url": url,
            "title": page_title,
            "heading": main_heading,
            "status": response.status_code,
        }

    except requests.RequestException as error:
        if verbose:
            print(f"Request failed for {url}: {error}")

        return {
            "url": url,
            "title": "Request Failed",
            "heading": "Request Failed",
            "status": None,
        }


def update_results(index, url, results, verbose):
    results[index] = scrape_resource(url, verbose)


def run_scraper():
    urls = [
        "https://docs.python.org/3/tutorial/",
        "https://docs.python.org/3/library/",
        "https://docs.python.org/3/reference/introduction.html",
    ]
    results = [None, None, None]
    threads = []

    for i, link in enumerate(urls):
        thread = threading.Thread(
            target=update_results,
            args=(i, link, results, True),
        )
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("\n=== Python Learning Resources ===")
    for index, result in enumerate(results, start=1):
        status = result["status"] if result["status"] is not None else "Unavailable"
        print(f"\n{index}. {result['title']}")
        print(f"   Heading: {result['heading']}")
        print(f"   Status: {status}")
        print(f"   URL: {result['url']}")


def main():
    print("=== Python Learning Resource Scraper ===")
    print("Fetching three official Python documentation pages...")
    run_scraper()


if __name__ == "__main__":
    main()
