from behave import step
from Pages.loginPages import loginPages as lp
from Pages.enquiryPages import enquiryPages as ep

@step("go to the salesforce test environment")
def navigateToSF(context):
    context.lp = lp(context.page)
    context.loop.run_until_complete(context.lp.goToSalesforce())


@step("give the username and password")
def enterCredentials(context):
    context.loop.run_until_complete(context.lp.enterUsername())
    context.loop.run_until_complete(context.lp.enterPassword())


@step("Click on the Login button")
def clickLoginButton(context):
    context.loop.run_until_complete(context.lp.clickLogin())


@step("verify the user is successfully able to login into the salesforce application")
def verifyLogin(context):
    try:
        context.loop.run_until_complete(context.lp.verifyLogin())

    except Exception as e:
        # 🔥 FORCE screenshot here (THIS WILL DEFINITELY RUN)
        context.loop.run_until_complete(
            context.page.screenshot(
                path="failure.png",
                full_page=True
            )
        )
        print("📸 Screenshot captured in step")
        raise e
    
    
@step("click on the Enquiry tab and click on the New button")
def clickEnquiryTab(context):
    context.ep = ep(context.page)
    context.loop.run_until_complete(context.ep.clickEnquiryTab())

@step("fill the mandatory fields and click on the save button")
def fillMandatoryFields(context):
    context.loop.run_until_complete(context.ep.screen1())
    context.loop.run_until_complete(context.ep.screen2())
    context.loop.run_until_complete(context.ep.screen3())

@step("verify the enquiry is created successfully")
def verifyEnquiry(context):
    context.loop.run_until_complete(context.ep.verifyEnquiry())

@step("add the interested location to the enquiry record and save it")
def addInterestedLocation(context):
    context.loop.run_until_complete(context.ep.addInterestedLocation())
    context.loop.run_until_complete(context.ep.EditInterestedLocation())

@step("Edit the enquiry and update the details and save the record")
def editEnquiry(context):
    context.loop.run_until_complete(context.ep.editEnquiry())

@step("Verify the user is successfully able to navigate to opportunity page")
def navigateToOpp(context):
    context.loop.run_until_complete(context.ep.navigateToOpp())
    