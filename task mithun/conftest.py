import os
import pytest
import pytest_asyncio
from playwright.async_api import async_playwright


@pytest_asyncio.fixture
async def async_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        yield page

        await browser.close()


@pytest_asyncio.fixture(autouse=True)
async def screenshot_on_failure(async_page, request):
    yield

    if (
        hasattr(request.node, "rep_call")
        and request.node.rep_call.failed
    ):
        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = os.path.join(
            "screenshots",
            f"{request.node.name}.png"
        )

        await async_page.screenshot(
            path=screenshot_path,
            full_page=True
        )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)