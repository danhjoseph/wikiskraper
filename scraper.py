import wikipedia


def wikiScraperSummary(url: str) -> str:
    """Scrape Wikipedia for a given article and return the summary"""

    res = wikipedia.summary({url})

    return res.replace("\n", "")


def wikiScraperImages(url: str) -> list:
    """Scrape Wikipedia for a given article and return the images"""

    res = wikipedia.page({url})

    return res.images


def wikiScraperContent(url: str) -> str:
    """Scrape Wikipedia for a given article and return the content"""

    res = wikipedia.page({url})

    return res.content.replace("\n", "")


def wikiScraperSection(url: str, section: str) -> str:
    """Scrape Wikipedia for a given article and return the section"""

    res = wikipedia.page({url})
    return res.section(section.capitalize())


def wikiScraperCategories(url: str) -> str:
    """Scrape Wikipedia for a given article and return the categories"""

    res = wikipedia.page({url})

    return res.categories
