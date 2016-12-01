Feature: Checking organization

Scenario: Create organization

  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When login ass owner
  Then user 'Behave Organization' was login successfully
  When click on My_organization button
  Then appear button Create_new_organization button
  When click on button 'Create_new_organization'
  When click on "Add New Organization"
  Then appear validation message "can't be blank"
