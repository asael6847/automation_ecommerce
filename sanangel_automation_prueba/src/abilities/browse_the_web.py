from playwright.sync_api import sync_playwright

class BrowseTheWeb:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False,args=["--start-maximized"])
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    def quit(self):
        self.browser.close()
        self.playwright.stop()