from bs4 import BeautifulSoup
import requests


def scrape_hp_site(
    scraper_api: str,
    api_key: str,
    url: str,
    render: str,
    screenshoot: str,
    retry_404: str,
    follow_redirect: str,
    wait_for_selector: str,
):
    payload = {
        "api_key": api_key,
        "url": url,
        "render": render,
        "screenshot": screenshoot,
        "retry_404": retry_404,
        "follow_redirect": follow_redirect,
        "wait_for_selector": wait_for_selector,
    }

    r = requests.get(scraper_api, params=payload)
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the div with the specific class
    div = soup.select(wait_for_selector)

    if div:
        # Extract text and remove the dollar sign
        price = div[0].text.strip().replace("$", "")
        return price
    else:
        return None
