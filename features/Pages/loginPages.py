class loginPages:

    def __init__(self, page):
        self.page = page

    async def goToSalesforce(self):
        await self.page.goto("https://test.salesforce.com/")

    async def enterUsername(self):
        await self.page.fill("#username", "ashwinimca96@gmail.com")

    async def enterPassword(self):
        await self.page.fill("#password", "RIS@2026")

    async def clickLogin(self):
        await self.page.click("#Login")

    async def verifyLogin(self):
     try:
       
        await self.page.get_by_title("All Warehouses").wait_for(timeout=30000)
      
        print("Login successful")
        await self.page.wait_for_timeout(5000)
        await self.page.context.storage_state(path="state.json")

     except Exception as e:
        await self.page.screenshot(path="debug_login_error.png", full_page=True)
        raise e