Feature: Checking organization

Scenario: Create organization

  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When login ass 'easyqa.thinkmobiles+10000@gmail.com','Go1234'
  Then user 'Behave Organization' was login successfully
  When click on My_organization button
  Then appear button Create_new_organization button