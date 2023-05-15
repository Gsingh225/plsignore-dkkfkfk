from playwright.sync_api import ViewportSize, sync_playwright
from playwright.async_api import async_playwright  # pylint: disable=unused-import

__all__=["picture"]

def picture():
    W,H = 1080, 900
    with sync_playwright as p:
        browser = p.chromium.launch(
            headless = False
        )
        dsf = (W//600) + 1
        context = browser.new_context(
            locale = "en-us",
            color_scheme = "dark",
            viewport=ViewportSize(width=W, height=H),
            device_scale_factor = dsf
            
        )
        page = context.new_page()
        page.goto("https://www.reddit.com/login", timeout=0)