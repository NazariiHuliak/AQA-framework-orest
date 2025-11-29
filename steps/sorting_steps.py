import time

from framework.dsl import given, when, then
from pages.search_results_page import SearchResultsPage

@when(r"I sort products by price '(.*)'")
def sort(ctx, order):
    results = ctx.pages["results"]
    if order == "asc":
        results.sort_by_price_asc()
    elif order == "desc":
        results.sort_by_price_desc()

    time.sleep(3)
    ctx.pages["results"] = SearchResultsPage(ctx.driver)

@then("should sort products by price '(.*)'")
def check(ctx, order):
    prices = ctx.pages["results"].get_prices()
    assert len(prices) > 0, "No search results found!"
    if order == "desc":
        assert prices[0] >= prices[1], "Products are not sorted by price desc"
    elif order == "asc":
        assert prices[0] <= prices[1], "Products are not sorted by price asc"


