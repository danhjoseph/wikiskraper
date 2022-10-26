from fastapi import FastAPI
import scraper


app = FastAPI()


@app.get("/")
def root():
    """Root API endpoint"""
    info = "Welcome to the Wikipedia Scraper Microservice. Please use the /wiki/ endpoint to scrape Wikipedia. For example, /wiki/RickAstley/summary will return the summary of the Rick Astley Wikipedia page, and /wiki/RickAstley/images will return the images of the Rick Astley Wikipedia page. The endpoints are /summary, /images, /content, /sections, and /categories. Please see the README for more information. I am a robot, I will never give up, I will never let you down, I will never run around and desert you, beep boop."
    return info


@app.get('/wiki/{article}/summary')
async def get_article(article: str):
    """Get article summary from wikipedia"""
    print("Getting summary for article: " + article)
    try:
        response = scraper.summary(article)
        print("Success!")
        return response
    except Exception as error:
        print("Error: " + str(error))
        response = "Error: " + str(error)
        return str(error)


@app.get('/wiki/{article}/images')
async def get_article_images(article: str):
    """Get article images from wikipedia"""
    print("Getting images for article: " + article)
    try:
        response = scraper.images(article)
        print("Success!")
        return response
    except Exception as error:
        print("Error: " + str(error))
        return str(error)


@app.get('/wiki/{article}/content')
async def get_article_content(article: str):
    """Get article content from wikipedia"""
    print("Getting content for article: " + article)
    try:
        response = scraper.content(article)
        print("Success!")
        return response
    except Exception as error:
        print("Error: " + str(error))
        return str(error)


@app.get('/wiki/{article}/{section}')
async def get_article_sections(article: str, section: str):
    """Get article sections from wikipedia"""
    print("Getting " + section + " for article: " + article)
    try:
        response = scraper.section(article, section)
        print("Success!")
        return response
    except Exception as error:
        print("Error: " + str(error))
        return str(error)


@app.get('/wiki/{article}/categories')
async def get_article_categories(article: str):
    """Get article categories from wikipedia"""
    print("Getting categories for article: " + article)
    try:
        response = scraper.categories(article)
        print("Success!")
        return response
    except Exception as error:
        print("Error: " + str(error))
        return str(error)

print("Server is listening on port 8000...")
