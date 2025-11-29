import time

from framework.dsl import given, when, then
from pages.search_results_page import SearchResultsPage

@when(r"I change language to '(.*)'")
def sort(ctx, lang_code):
    results = ctx.pages["results"]
    results.change_language()
    ctx.pages["results"] = SearchResultsPage(ctx.driver)

@then("language should be '(.*)'")
def check(ctx, expected_lang):
    lang = ctx.pages["results"].get_language()
    assert lang.lower() == expected_lang.lower(), f"Expected language '{expected_lang}', but got '{lang}'"



