*** Settings ***
Resource          ../Keywords/headless_resource.robot
*** Test Cases ***
Invalid Login
    Navigate to Homepage
    Input Username    x
    Input Password    x
    Submit User Credentials
    Homepage Should Have Valid Title
    [Teardown]    Close Browser