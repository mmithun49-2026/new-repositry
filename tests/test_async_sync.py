#Navigate to the facebook.com need to validate(Title of the page)
#navigate CMD
#.env and requirements files
import pytest
from playwright.sync_api import sync_playwright,expect
# from playwright.async_api import async_playwright,expect
import asyncio
#Sync mode
# def test_sync_sync_exp1():
#     with sync_playwright() as p:
#         #chrome browser
#         browser=p.chromium.launch(headless=False)
#         user_context=browser.new_context()
#         page=user_context.new_page()
#         page.goto("https://www.facebook.com/")
#         print(page.title()) #gives the title of the page
#         expect(page).to_have_title("Facebook")
#     #test -->Banking
#     #login as user
#     #login as manager


# #Async mode
# async def test_async_sync_exp2():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         user_context = await browser.new_context()
#         page = await user_context.new_page()
#         await page.goto("https://www.facebook.com/")
#         print(page.title())  # gives the title of the page
#         await expect(page).to_have_title("Facebook")
# # asyncio.run(test_async_sync_exp2())
#         # - anyio
#         # - pytest - asyncio
#         # - pytest - tornasync
#         # - pytest - trio
#         # - pytest - twisted
# from playwright.async_api import expect
def test_async_sync_exp3():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        user_context=browser.new_context()
        page=user_context.new_page()
        page.goto('https://www.facebook.com/')
        print(page.title())
        expect(page).to_have_title("Facebook")
        page.goto("https://www.amazon.in/")
        expect(page).to_have_url("https://www.amazon.in/")
        page.go_back()
        page.go_forward()
        page.reload()

# @pytest.mark.asyncio
# async def test_async_sync_exp4(page):
#     await page.goto('https://www.facebook.com/')
#     print(await page.title())
#     await expect(page).to_have_title("Facebook")