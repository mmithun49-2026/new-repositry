# import pytest
# from playwright.async_api import expect
# @pytest.mark.asyncio
# async def test_check_box(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     check_locator = async_page.locator("//div[@class='form-check form-check-inline']//input[@type='checkbox']/following-sibling::label")
#     await expect(check_locator.first).not_to_be_checked()
#     await check_locator.first.check()
#     await expect(check_locator.first).to_be_checked()
#     all_check_boxes = await check_locator.all_inner_texts()
#     print(all_check_boxes)


# @pytest.mark.asyncio
# async def test_check_box_input_list(async_page):
#     text_check_box = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     for i in text_check_box:
#         check_locator = async_page.locator(f"//input[@id='{i.lower()}']")
#         await expect(check_locator).not_to_be_checked()
#         await check_locator.check()
#         await expect(check_locator).to_be_checked()
# from playwright.async_api import expect


# @pytest.mark.asyncio
# async def test_check_box_input_list(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     async_page.once(
#         "dialog",lambda dialog:(
#            print("type of alert = " , dialog.type),
#             print("msg = " , dialog.message),
#             dialog.accept()
#         )
#     )
#     await async_page.get_by_text("Simple Alert").click()
#
#     ele = async_page.locator("#sunday")
#     await  expect(ele).not_to_be_checked()
#     await ele.click()
#     await  expect(ele).to_be_checked()
import pytest
from playwright.async_api import expect
# async def handle_aletrs(dialog):
#     print("alert type = " , dialog.type)
#     print("alter msg" , dialog.message)
#     await dialog.accept()
#
#
# @pytest.mark.asyncio
# async def test_alert(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     async_page.on("dialog", handle_aletrs)
#     await async_page.get_by_text("Confirmation Alert").click()
#
#     ele = async_page.locator("#sunday")
#     await  expect(ele).not_to_be_checked()
#     await ele.click()
#     await  expect(ele).to_be_checked()


# @pytest.mark.asyncio
# async def test_mul_wiind(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     search_box = async_page.locator("#twotabsearchtextbox")
#     await search_box.fill("Books")
#     await search_box.press("Enter")
#     await async_page.wait_for_timeout(5000)
#     books = async_page.locator("//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")
#
#     # need get the wind info
#     async with async_page.expect_popup() as pop_info:
#         await books.first.click()
#
#     product_page = await pop_info.value
#     await product_page.locator("//input[@id='add-to-cart-button']").click()

@pytest.mark.asyncio
async def test_mul_wiind(async_page):
    await async_page.goto("https://www.amazon.in/")

    search_box = async_page.locator("#twotabsearchtextbox")
    await search_box.fill("Books")
    await search_box.press("Enter")

    # Wait for search results to load properly instead of a fixed timeout
    books = async_page.locator("h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal")
    await books.first.wait_for(state="visible")

    # Handle the first product click (if it opens a new tab/window)
    async with async_page.expect_popup() as pop_info:
        await books.first.click()

    product_page = await pop_info.value
    await product_page.wait_for_load_state("domcontentloaded")

    # Click 'Add to Cart' (stays on the same product page or opens a side sheet)
    add_to_cart_btn = product_page.locator("//input[@id='add-to-cart-button']")
    await add_to_cart_btn.click()

    # Wait for the cart confirmation / side panel / elements to update
    # If Amazon prompts a specific cart sub-page or "Proceed to Checkout" button:
    checkout_button = product_page.locator(
        "//input[@name='proceedToRetailCheckout' or @data-feature-id='proceed-to-checkout-action']")
    await checkout_button.wait_for(state="visible")
    await checkout_button.click()