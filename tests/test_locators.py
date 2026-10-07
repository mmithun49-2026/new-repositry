# import pytest
# from tests.utils.config import BASE_URL
#
# @pytest.mark.asyncio
# async def test_env(async_page):
#     await async_page.goto(BASE_URL)
#     print(await async_page.title())
#
# import pytest
# from playwright.async_api import expect
# @pytest.mark.asyncio
# async def test_getbyrole(async_page):
#     await async_page.goto(https://demowebshop.tricentis.com/)
#
#     register_link= async def test_getbyrole("link","register"):
#         expect(reg_link).to_be_visible()
#         reg_link.click()

# import pytest
# from playwright.async_api import expect
#
# @pytest.mark.asyncio
# async def test_getbyrole(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#
#     reg_link = async_page.get_by_role("link", name="Register")
#     await expect(reg_link).to_be_visible()
#     await reg_link.click()


# import asyncio
# from playwright.async_api import async_playwright
#
#
# async def test_getbyrole():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#
#         await page.goto("https://demowebshop.tricentis.com/")
#
#         reg_link = page.get_by_role("link", name="Register")
#
#         await reg_link.wait_for()
#         await reg_link.click()
#
#
#
#
# asyncio.run(test_getbyrole())
#
# import pytest
from playwright.async_api import expect


# @pytest.mark.asyncio
# async def test_getByText(async_page):
#
#     await async_page.goto("https://demowebshop.tricentis.com/")
#
#     excellent = async_page.get_by_role("radio", name="Excellent")
#
#
#     await expect(excellent).to_be_visible()
#     await excellent.click()
#
#     await async_page.wait_for_timeout(5000)
#
#     vb = async_page.get_by_role("radio", name="Very bad")
#
#     await expect(vb).to_be_visible()
#     await vb.click()
#
#     await expect(vb).to_be_checked()
#


   # page.getByLabel() to locate a form control by associated label's text.
   # @pytest.mark.asyncio
   # async def test_getBylabel(async_page):
   #     await async_page.goto("https://demowebshop.tricentis.com/")
   #     reg_link = async_page.get_by_text("Register")
   #     await expect(reg_link).to_be_visible()
   #     await reg_link.click()
   #     g = async_page.get_by_text("Female")
   #     await expect(g).to_be_visible()
   #     await g.click()
   #     fn = async_page.get_by_label("First name:")
   #     await expect(fn).to_be_visible()
   #     await fn.fill("Abc")
   #     ln = async_page.get_by_label("Last name:")
   #     await expect(ln).to_be_visible()
   #     await ln.fill("Abc")
   #     email = async_page.get_by_label("Email:")
   #     await expect(email).to_be_visible()
   #     await email.fill("abc@gmail.com")
   #     pwd = async_page.get_by_label("Password:").nth(0)  # [pwd,cpwd]
   #     await expect(pwd).to_be_visible()
   #     await pwd.fill("Abc@123")
   #     cpwd = async_page.get_by_label("Confirm password:")
   #     await expect(cpwd).to_be_visible()
   #     await cpwd.fill("Abc@123")


import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_get_by_label(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")

    # Register
    reg_link = async_page.get_by_role("link", name="Register")
    await expect(reg_link).to_be_visible()
    await reg_link.click()

    # Gender
    female = async_page.get_by_label("Female")
    await expect(female).to_be_visible()
    await female.check()
    await expect(female).to_be_checked()

    # First Name
    fn = async_page.get_by_label("First name:")
    await expect(fn).to_be_visible()
    await fn.fill("Abc")

    # Last Name
    ln = async_page.get_by_label("Last name:")
    await expect(ln).to_be_visible()
    await ln.fill("Abc")

    # Email
    email = async_page.get_by_label("Email:")
    await expect(email).to_be_visible()
    await email.fill("abc@gmail.com")

    # Password
    pwd = async_page.get_by_label("Password:")
    await expect(pwd).to_be_visible()
    await pwd.fill("Abc@123")

    # Confirm Password
    cpwd = async_page.get_by_label("Confirm password:")
    await expect(cpwd).to_be_visible()
    await cpwd.fill("Abc@123")
    await async_page.wait_for_timeout(10000)

