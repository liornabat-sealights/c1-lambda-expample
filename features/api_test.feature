Feature: Testing Lambda Function API Endpoints

Scenario: Test /health Success
  Given valid AWS connection
  When API call (No Data): '/health'
  Then expect status: '200'

Scenario: Test /sendRatesToCustomizer Success
  Given valid AWS connection
  When API call (No Data): '/sendRatesToCustomizer'
  Then expect status: '200'

Scenario: Test /sendRatesToCustomizer Fail - Invalid DPAPI Request
  Given valid AWS connection
  When API call (Data): '/sendRatesToCustomizer'
  """
  {}
  """
  Then expect status: '200'
  And raise: 'RatesException'

