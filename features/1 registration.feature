Feature: Checking Registration

Scenario: Сheck registration with valid data

  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When click on Sign up tab
  When fill registration form 'Oleg', 'Stasiv', 'easyqa.thinkmobiles@gmail.com', 'Webdriver', 'Ukraine', '123456'
  When click on button SignUp
  Then user 'Oleg Stasiv' was register successfully

Scenario: Сheck registration with empty fields

  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When click on Sign up tab
  When fill email field 'easyqa.thinkmobiles'
  When click on button SignUp
  Then appear validation messages 'is invalid'
