import os
import asyncio
from playwright.async_api import async_playwright


def before_all(context):
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)


def before_scenario(context, scenario):

    async def setup():
        context.playwright = await async_playwright().start()
        context.browser = await context.playwright.chromium.launch(headless=True)

        try:
            context.context = await context.browser.new_context(storage_state="state.json")
        except:
            context.context = await context.browser.new_context()

        context.page = await context.context.new_page()

    context.loop.run_until_complete(setup())


def after_step(context, step):
    """
    Takes screenshot automatically when a step fails
    """
    if step.status == "failed":
        os.makedirs("screenshots", exist_ok=True)

        if hasattr(context, "page"):
            context.page.screenshot(
                path=f"screenshots/{step.name}.png",
                full_page=True
            )

        print(f"❌ Screenshot captured for failed step: {step.name}")


def after_scenario(context, scenario):

    async def teardown():
        if hasattr(context, "context"):
            await context.context.close()

        if hasattr(context, "browser"):
            await context.browser.close()

        if hasattr(context, "playwright"):
            await context.playwright.stop()

    context.loop.run_until_complete(teardown())


def after_all(context):
    context.loop.close()