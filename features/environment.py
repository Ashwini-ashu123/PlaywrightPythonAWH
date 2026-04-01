import asyncio
from playwright.async_api import async_playwright

def before_scenario(context, scenario):
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)

    HEADLESS = True   

    async def setup():
        context.playwright = await async_playwright().start()

       
        context.browser = await context.playwright.chromium.launch(headless=HEADLESS)

       
        context.context = await context.browser.new_context(storage_state="state.json")

        context.page = await context.context.new_page()

        await context.page.goto("https://test.salesforce.com/home/home.jsp")

    context.loop.run_until_complete(setup())


def after_scenario(context, scenario):
    async def teardown():
        await context.context.close()
        await context.browser.close()
        await context.playwright.stop()

    context.loop.run_until_complete(teardown())