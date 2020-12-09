*** Settings ***
Resource          Robot Tests/Keywords/headless_resource.robot
*** Test Cases ***
Valid Login
    Navigate to Homepage
    Input Username    user
    Input Password    holden
    Submit User Credentials
    Dashboard Page Should Have Valid Title   Muppet Musical :P
    [Teardown]    Close Browser