import wikipedia


def summary(url: str) -> str:
    """Scrape Wikipedia for a given article and return the summary"""

    res = wikipedia.summary({url})

    return res.replace("\n", "")


def images(url: str) -> list:
    """Scrape Wikipedia for a given article and return the images"""

    res = wikipedia.page({url})

    return res.images


def content(url: str) -> str:
    """Scrape Wikipedia for a given article and return the content"""

    res = wikipedia.page({url})

    return res.content.replace("\n", "")


def section(url: str, section: str) -> str:
    """Scrape Wikipedia for a given article and return the section"""

    res = wikipedia.page({url})
    return res.section(section.capitalize())


def categories(url: str) -> str:
    """Scrape Wikipedia for a given article and return the categories"""

    res = wikipedia.page({url})

    return res.categories
