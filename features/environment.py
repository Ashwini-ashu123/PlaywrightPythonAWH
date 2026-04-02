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


# 🔥 MAIN FIX — RELIABLE SCREENSHOT HOOK
def after_step(context, step):
    if step.status == "failed":
        os.makedirs("screenshots", exist_ok=True)

        async def take_screenshot():
            try:
                if hasattr(context, "page") and context.page:
                    await context.page.wait_for_timeout(1000)  # stabilize page
                    await context.page.screenshot(
                        path=f"screenshots/{step.name}.png",
                        full_page=True
                    )
                    print(f"✅ Screenshot captured: {step.name}")
            except Exception as e:
                print(f"❌ Screenshot failed: {e}")

        context.loop.run_until_complete(take_screenshot())


def after_scenario(context, scenario):

    async def teardown():
        try:
            # 🔥 IMPORTANT: wait if failed (prevents early close)
            if scenario.status == "failed" and hasattr(context, "page"):
                print("⏳ Waiting before closing browser (failure case)")
                await context.page.wait_for_timeout(3000)

            if hasattr(context, "context"):
                await context.context.close()

            if hasattr(context, "browser"):
                await context.browser.close()

            if hasattr(context, "playwright"):
                await context.playwright.stop()

        except Exception as e:
            print(f"Teardown error: {e}")

    context.loop.run_until_complete(teardown())


def after_all(context):
    context.loop.close()