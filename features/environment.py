import os
import asyncio
from playwright.async_api import async_playwright


def before_all(context):
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)


def before_scenario(context, scenario):
    async def setup():
        context.playwright = await async_playwright().start()
        context.browser = await context.playwright.chromium.launch(headless=False)
        context.context = await context.browser.new_context()
        context.page = await context.context.new_page()

    context.loop.run_until_complete(setup())



def after_step(context, step):
    if step.status == "failed":
        os.makedirs("screenshots", exist_ok=True)

        try:
            context.loop.run_until_complete(
                context.page.screenshot(
                    path="screenshots/failure.png",
                    full_page=True
                )
            )
            print("📸 Screenshot saved")

        except Exception as e:
            print("❌ Screenshot failed:", e)


def after_scenario(context, scenario):
    async def teardown():
        await context.browser.close()
        await context.playwright.stop()

    context.loop.run_until_complete(teardown())


def after_all(context):
    context.loop.close()