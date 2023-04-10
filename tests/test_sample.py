from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://5controls.com/")
    page.get_by_role("button", name="Yes, I agree").click()
    page.get_by_role("link", name="Go to slide 5").click()
    page.get_by_text("Suddenly run out of stock? Our min/MAX system ensures that the stock level is al").click()
    page.locator("#contact").click()
    page.get_by_placeholder("Business email*").click()
    page.get_by_placeholder("Business email*").fill("sdvsv")
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("sdvsdv")
    page.get_by_placeholder("Company").click()
    page.get_by_placeholder("Company").fill("sdvsdv")
    page.get_by_label("Errors in calculation and measurement").check()
    page.get_by_label("Incorrect labelling/assembly").check()
    page.get_by_label("Lost inventory").check()
    page.get_by_label("Wasting time on locating an employee, absenteeism").check()
    page.get_by_label("Poor safety").check()
    page.get_by_label("Idle staff").check()
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("link", name="free trial").click()
    page.screenshot(path='test-results/testpy.jpg')
    
#     import pytest
# from playwright.sync_api import Playwright, sync_playwright


# @pytest.mark.playwright
# def test_example() -> None:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         with browser.new_context() as context:
#             page = context.new_page()
#             page.goto("https://5controls.com/")
#             page.get_by_role("button", name="Yes, I agree").click()
#             page.get_by_role("link", name="Go to slide 5").click()
#             page.get_by_text("Suddenly run out of stock? Our min/MAX system ensures that the stock level is al").click()
#             page.locator("#contact").click()
#             page.get_by_placeholder("Business email*").click()
#             page.get_by_placeholder("Business email*").fill("sdvsv")
#             page.get_by_placeholder("Name").click()
#             page.get_by_placeholder("Name").fill("sdvsdv")
#             page.get_by_placeholder("Company").click()
#             page.get_by_placeholder("Company").fill("sdvsdv")
#             page.get_by_label("Errors in calculation and measurement").check()
#             page.get_by_label("Incorrect labelling/assembly").check()
#             page.get_by_label("Lost inventory").check()
#             page.get_by_label("Wasting time on locating an employee, absenteeism").check()
#             page.get_by_label("Poor safety").check()
#             page.get_by_label("Idle staff").check()
#             page.get_by_role("button", name="Submit").click()
#             page.get_by_role("link", name="free trial").click()
#             page.screenshot(path='test-results/test.jpg')
    