from playwright.sync_api import Playwright, sync_playwright, expect



def test_contact_form(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    f = open('container_ip.txt', 'r')
    cip = f.read().strip()
    f.close()
    ip ="http://"+cip+":8080/"
    print(ip)
    page.goto(ip, timeout = 60*1000*3)
    page.get_by_role("link", name="Contact").click()
    page.locator("input[name=\"name\"]").click()
    page.locator("input[name=\"name\"]").fill("test")
    expect(page.locator("input[name=\"name\"]")).to_have_value("test")
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("test@test.com")
    expect(page.locator("input[name=\"email\"]")).to_have_value("test@test.com")
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("123")
    page.locator("textarea[name=\"message\"]").click()
    page.locator("textarea[name=\"message\"]").fill("123")
    expect(page.locator("textarea[name=\"message\"]")).to_have_value("123")
    page.get_by_role("button", name="Submit").click()
    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_contact_form(playwright)
