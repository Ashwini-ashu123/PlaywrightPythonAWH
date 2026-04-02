Feature: Salesforce login

@skip_ci
Scenario: Login into the salesforce uat org
Given go to the salesforce test environment 
Then give the username and password
And Click on the Login button
And verify the user is successfully able to login into the salesforce application
Then click on the Enquiry tab and click on the New button
And fill the mandatory fields and click on the save button
And verify the enquiry is created successfully
Then add the interested location to the enquiry record and save it
Then Edit the enquiry and update the details and save the record
And Verify the user is successfully able to navigate to opportunity page
