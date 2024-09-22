from typing import Any
import requests
import sys
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import pandas as pd


def extract_fields(el) -> dict[str, Any]:
    visible_part = el.find('a', class_='multitrack-schedule__single')
    hidden_part = el.find('div', class_="reveal-modal")
    return {
        "title": visible_part.find('h4').get_text().strip(),
        "speakers_names": visible_part.find('p', class_='speakers').get_text().strip(),
        "summary": md(
            "".join(
                str(el) for el
                in hidden_part.find('div', class_='session-overview-markdown').contents
            )
        ).strip(),
        # "visible": visible_part,
        # "hidden": hidden_part,
        # TODO?: maybe add: 'advanced|beginner|...' label; tags, like "<span class="radius label tag">idris</span>"
    }

def retrieve_sections(url) -> list[dict]:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    slots = soup.find_all('tr', class_='slot')

    return sum([slot.find_all('td', class_='placement') for slot in slots], [])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python extraction.py <archive_url>", file=sys.stderr)
        sys.exit(1)

    # archive_url = "https://web.archive.org/web/20220930063625/https://skillsmatter.com/conferences/11741-haskell-exchange-2019"
    archive_url = sys.argv[1]
    title = archive_url.split('/')[-1]

    items = retrieve_sections(archive_url)

    table = pd.DataFrame(extract_fields(item) for item in items)
    table.to_csv(f"outputs/{title}.csv", index=False, sep="\t")
    exit(0)
