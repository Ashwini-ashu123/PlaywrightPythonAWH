import asyncio
from playwright.async_api import async_playwright

def before_scenario(context, scenario):
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)

    HEADLESS = False  

    async def setup():
        context.playwright = await async_playwright().start()

        context.browser = await context.playwright.chromium.launch_persistent_context(
            user_data_dir="C:/Users/Aswini/playwright-profile",
            headless=HEADLESS
        )

        context.page = context.browser.pages[0] if context.browser.pages else await context.browser.new_page()

      
        await context.page.goto("https://test.salesforce.com/home/home.jsp")

   
    context.loop.run_until_complete(setup())


def after_scenario(context, scenario):
    async def teardown():
        await context.browser.close()
        await context.playwright.stop()

    context.loop.run_until_complete(teardown())