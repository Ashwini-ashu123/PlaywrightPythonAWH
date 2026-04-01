import asyncio
from playwright.async_api import async_playwright

def before_all(context):
    """
    Runs once before all scenarios
    """
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)


def before_scenario(context, scenario):
    """
    Runs before each scenario - launches browser and creates context/page
    """

    async def setup():
        context.playwright = await async_playwright().start()

        # Launch browser (headless can be set False for debugging)
        context.browser = await context.playwright.chromium.launch(headless=True)

        # If state.json exists, it will reuse login/session
        try:
            context.context = await context.browser.new_context(storage_state="state.json")
        except:
            context.context = await context.browser.new_context()

        context.page = await context.context.new_page()

    context.loop.run_until_complete(setup())


def after_scenario(context, scenario):
    """
    Runs after each scenario - cleanup
    """

    async def teardown():
        if hasattr(context, "context"):
            await context.context.close()

        if hasattr(context, "browser"):
            await context.browser.close()

        if hasattr(context, "playwright"):
            await context.playwright.stop()

    context.loop.run_until_complete(teardown())


def after_all(context):
    """
    Final cleanup
    """
    context.loop.close()