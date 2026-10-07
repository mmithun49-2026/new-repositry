# import pytest
# from playwright.async_api import expect
#
# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    ele = async_page.get_by_text("Welcome to our store")
#    await expect(ele).to_be_visible()

 # import pytest
 #from playwright.async_api import expect
#
# @pytest.mark.asyncio
# async def test_welcome_message_is_visible(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#
#     element = async_page.get_by_text("Welcome to our store")
#     await expect(element).to_be_visible()

# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    ele = async_page.locator("h2[class='topic-html-content-header']") # locator :notfinding
#    await expect(ele).to_be_visible()
#    await expect(ele).to_be_visible(timeout=30000)
#    print(ele.inner_html())
import pytest
from playwright.async_api import expect
# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    ele = async_page.locator("input[class='button-2 product-box-add-to-cart-button']") # locator :notfinding
#    all_product = await ele.all()
#    for i in all_product:
#        await i.click()
#        break
#    await async_page.wait_for_timeout(5000)


import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_select_samsung_phone(async_page):

    # Open Amazon India
    await async_page.goto("https://www.amazon.in/")

    # Search for Samsung phone
    search_box = async_page.get_by_placeholder("Search Amazon.in")
    await search_box.fill("Samsung phone")
    await search_box.press("Enter")

    # Wait for search results
    await async_page.wait_for_load_state("domcontentloaded")

    # Select a Samsung phone from the results
    samsung_phone = async_page.get_by_text("Samsung", exact=False).first
    await samsung_phone.click()

    # Keep browser open for debugging
    await async_page.wait_for_timeout(5000)



import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_select_samsung_phone(async_page):

    await async_page.goto("https://www.amazon.in/")

    await async_page.locator("#twotabsearchtextbox").fill("Samsung phone")
    await async_page.locator("#nav-search-submit-button").click()

    await async_page.wait_for_load_state("domcontentloaded")

    # Locate Samsung product results
    products = async_page.locator('[data-component-type="s-search-result"]')

    await expect(products.first).to_be_visible(timeout=30000)

    print("Number of products:", await products.count())

    # Click the first product
    await products.first.locator("h2 a").click()

    await async_page.wait_for_timeout(5000)
#