Feature: Checking loginization

Scenario: Сheck login with valid user

  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When enter email which was registered
  When enter password '123456'
  When click on button SignIn
  Then user 'Oleg Stasiv' was login successfully

Scenario: Сheck login with invalid user

  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When enter email which was registered
  When enter password 'yana2468975311'
  When click on button SignIn
  Then appear validation message 'Invalid Email or password.'

Scenario: Forgot Password
  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When click on Forgot link
  Then appears Forgot field
  When enter existing email
  When click on Restore button
  Then email was send on your mail box
  When click on reset link
  Then appears Password restore fields
  When enter new password '123456'
  When click on Change my password button
  Then should redirect on Login screen
  Given website "http://qa_dashboard.test.thinkmobiles.com:8085"
  When enter email which was registered
  When enter password '123456'
  When click on button SignIn
  Then user 'Oleg Stasiv' was login successfully

