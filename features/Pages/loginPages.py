class loginPages:

    def __init__(self, page):
        self.page = page

    async def goToSalesforce(self):
        await self.page.goto("https://test.salesforce.com/")

    async def enterUsername(self):
        await self.page.fill("#username", "awhris@salesforce.com.uat")

    async def enterPassword(self):
        await self.page.fill("#password", "RIS@2026")

    async def clickLogin(self):
        await self.page.click("#Login")

    async def verifyLogin(self):
        await self.page.get_by_title("All Warehouses").wait_for(timeout=10000)