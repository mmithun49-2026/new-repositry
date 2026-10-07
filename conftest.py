import pytest
from playwright.async_api import async_playwright
# import pytest_asyncio
# @pytest_asyncio.fixture
# # #
# async def async_page():
#    async with async_playwright() as p:
#        browser=await p.chromium.launch(headless=True)
#        page=await browser.new_page()
#        yield page #generator object
#        await browser.close()
#
from playwright.async_api import async_playwright
import pytest_asyncio

@pytest_asyncio.fixture
async def async_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) #
        page = await browser.new_page() # page
        yield  page
        await browser.close()


@pytest_asyncio.fixture
async def chromium_page():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        context = await browser.new_context()

        page = await context.new_page()

        yield page

        await context.close()
        await browser.close()


@pytest_asyncio.fixture
async def firefox_page():

    async with async_playwright() as p:

        browser = await p.firefox.launch(
            headless=False
        )

        context = await browser.new_context()

        page = await context.new_page()

        yield page

        await context.close()
        await browser.close()

@pytest_asyncio.fixture
async def webkit_page():

    async with async_playwright() as p:

        browser = await p.webkit.launch(
            headless=False
        )

        context = await browser.new_context()

        page = await context.new_page()

        yield page

        await context.close()
        await browser.close()