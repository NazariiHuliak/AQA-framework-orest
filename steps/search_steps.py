import time

from framework.dsl import given, when, then
from pages.search_results_page import SearchResultsPage

@when(r"I search for '(.*)'")
def search(ctx, query):
    home = ctx.pages["home"]
    home.search(query)
    ctx.pages["results"] = SearchResultsPage(ctx.driver)

@then("search results should contain '(.*)'")
def check(ctx, query):
    titles = ctx.pages["results"].get_titles()
    assert len(titles) > 0, "No search results found!"

    matching = [t for t in titles if query.lower() in t.lower()]
    assert len(matching) > 0, f"No search results contain '{query}'"
