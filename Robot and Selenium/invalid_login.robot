*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Valid Login
    Navigate to Homepage
    Input Username    x
    Input Password    x
    Submit User Credentials
    Homepage Should Have Valid Title
    [Teardown]    Close Browser