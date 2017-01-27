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
  When create organization "Test one" and Description "Test description"
  Then My organization list contain "Test one" organization

Scenario: Edit organization

  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When login ass owner
  When click on My_organization button
  When click on My organization in Left Menu
  When click on organization
  When click on Change button
  When edit organization "Test one edit" and Description "Test description edit"
  When click on Save changes button
  When click on My_organization button
  Then My organization list contain "Test one edit" organization

Scenario: Delete organization
  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When login ass owner
  When click on My_organization button
  When click on organization "Test one edit"
  When click on "Delete organization" button in left menu
  When click on "Delete organization" button
  Then appears popup window "Delete?"
  When click on "Delete" button in popup
  Then My organization list not contain "Test one edit" organization

Scenario: Add user to organization
  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When login ass owner
  When click on My_organization button
  When clear all organization
  When create organization "Test one edit"
  When click on organization "Test one edit"
  When click on "Organization Members" button in left menu
  When click on "Add Members" button
  Then appears popup window "Add Organization Members"
