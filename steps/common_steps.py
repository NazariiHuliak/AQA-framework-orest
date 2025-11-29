from framework.dsl import given, when, then
from pages.home_page import HomePage

@given("I open the Rozetka home page")
def open_home(ctx):
    ctx.pages["home"] = HomePage(ctx.driver)
    ctx.pages["home"].open_home()
