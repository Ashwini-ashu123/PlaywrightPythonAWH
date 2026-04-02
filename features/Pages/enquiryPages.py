class enquiryPages:

  enquiryName ="Maria"

  def __init__(self,page):
    self.page = page

  async def clickEnquiryTab(self):
    try:
        await self.page.wait_for_timeout(20000)

        await self.page.screenshot(path="debug_enquiry_start.png")

        await self.page.get_by_title("All Warehouses").wait_for(timeout=10000)
        await self.page.get_by_title("Enquiries").click()

        print("enquiry tab is clicked")

        await self.page.get_by_role("button", name="New").click()
        print("new button is clicked")

    except Exception as e:
        await self.page.screenshot(path="debug_enquiry_error.png", full_page=True)
        raise e


  async def screen1(self):
    await self.page.get_by_placeholder("Enter Mobile Number").fill("2345654544")
    print("mobile number is entered")
    await self.page.get_by_placeholder("you@example.com").fill("xyz@ywe.com")
    print("email is entered")
    await self.page.get_by_role("button", name="Next").click()
    print("next button is clicked")

  async def screen2(self):
    await self.page.get_by_placeholder("Last Name").fill(enquiryPages.enquiryName)
    print("last name is entered")
    await self.page.get_by_role("button", name="Save").click()
    print("save button is clicked")
    await self.page.select_option('[name="Intent_Type"]', label="Tenant")
    print("intent type is selected")
    await self.page.get_by_role("button", name="Next").click()

  async  def screen3(self):
    await self.page.fill('[name="Budget_Range1__c"]', "45000")
    print("budget range is entered")
    await self.page.fill('[name="Size_in_sqfts__c"]',"2000")
    print("size in sqfts is entered")
    await self.page.get_by_role("combobox", name="Nature of Purchase").click()
    await self.page.get_by_role("option", name="Rent").click()
    print("nature of purchase is selected")
    await self.page.get_by_role("combobox", name="Service Required").click()
    await self.page.get_by_role("option", name="Shed").click()
    print("service required is selected")
    await self.page.get_by_role("combobox", name="Enquiry Source").click()
    await self.page.get_by_role("option", name="Offline").click()
    print("enquiry source is selected")
    await self.page.get_by_role("combobox", name="Enquiry Sub Source").click()
    await self.page.get_by_role("option", name="Walk-in").click()
    print("enquiry sub source is selected")
    await self.page.get_by_role("button", name="Next").click()

  async def verifyEnquiry(self):
    name = await self.page.locator("h1 lightning-formatted-text").text_content()
    assert name == enquiryPages.enquiryName
    print("enquiry is created successfully", name)


  async def addInterestedLocation(self):
    scrollable = self.page.locator("flexipage-record-home-scrollable-column.col.main-col.slds-col")
    await scrollable.evaluate("""el => {
          el.scrollBy(0, 500);
        }
    """)
    print("mouse is moved")
    await self.page.wait_for_timeout(3000) 
    await self.page.locator("//button[@name='New']").click()
    print("new button is clicked")


  async def EditInterestedLocation(self):
    await self.page.get_by_label("Interested Locations Name").fill("Parrys")
    print("interested location name is entered")
    await self.page.get_by_label("Interested Location Range").fill("25")
    print("interested location range is entered")
    await self.page.locator("//button[@name='SaveEdit']").click()
    print("save button is clicked")

  async def editEnquiry(self):
    scrollable = self.page.locator("flexipage-record-home-scrollable-column.col.main-col.slds-col")
    await scrollable.evaluate("""el => {
          el.scrollBy(0, -500);
        }
    """)
    print("mouse is moved to top")
    await self.page.locator("//button[@name='Edit']").click()
    print("edit button is clicked")
    await self.page.get_by_role("combobox", name="Size Range").click()
    await self.page.get_by_role("option",name="below 10000").click()
    print("size range is updated")
    await self.page.get_by_role("combobox", name="Status").click()
    await self.page.get_by_role("option",name="Closed").click()
    print("status is updated")
    await self.page.get_by_role("combobox", name="Reason for Closed").click()
    await self.page.get_by_role("option", name="Qualified",exact=True).click()
    print("reason for closed is updated")
    await self.page.locator("//button[@name='SaveEdit']").click()
    print("save button is clicked")
   

   

  async def navigateToOpp(self):
    await self.page.get_by_role("button", name="Submit").click()
    print("submit button is clicked")
    await self.page.wait_for_timeout(5000) 
    Opp = await self.page.locator("records-entity-label",  has_text="Opportunities").text_content()
    assert Opp == "Opportunities"
    print("user is successfully navigated to opportunity page", Opp)
    Oppname =await self.page.locator("h1 lightning-formatted-text", has_text=enquiryPages.enquiryName).nth(1).text_content()
    assert Oppname == enquiryPages.enquiryName
    print("opportunity is created successfully", Oppname, Opp)



