import os
import asyncio
from playwright.async_api import async_playwright


def before_all(context):
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)


def before_scenario(context, scenario):
    async def setup():
        context.playwright = await async_playwright().start()
        context.browser = await context.playwright.chromium.launch(headless=False)  # keep false for debugging

        try:
            context.context = await context.browser.new_context(storage_state="state.json")
        except:
            context.context = await context.browser.new_context()

        context.page = await context.context.new_page()

    context.loop.run_until_complete(setup())


# 🔥 THIS IS THE MAIN FIX
def after_step(context, step):
    if step.status == "failed":
        os.makedirs("screenshots", exist_ok=True)

        async def take_screenshot():
            try:
                await context.page.screenshot(
                    path=f"screenshots/{step.name}.png",
                    full_page=True
                )
                print(f"📸 Screenshot captured: {step.name}")
            except Exception as e:
                print(f"Screenshot error: {e}")

        context.loop.run_until_complete(take_screenshot())


def after_scenario(context, scenario):
    async def teardown():
        await context.context.close()
        await context.browser.close()
        await context.playwright.stop()

    context.loop.run_until_complete(teardown())


def after_all(context):
    context.loop.close()