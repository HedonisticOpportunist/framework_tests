*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${DELAY}          0
${SIGN_UP}      https://hedonisticopportunist.github.io/framework_tests/site/login.html
${DASHBOARD}    https://hedonisticopportunist.github.io/framework_tests/site/dashboard.html

*** Keywords ***

Navigate to Homepage
    Open Browser    ${SIGN_UP}    headlesschrome
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Homepage Should Have Valid Title

Homepage Should Have Valid Title
    Title Should Be   Login 💀

Input Username
    [Arguments]   ${username}
    Input Text    //*[@id="username"]    ${username}

Input Password
    [Arguments]   ${password}
    Input Text    //*[@id="password"]    ${password}

Submit User Credentials
    Click Button    Login

Dashboard Page Should Have Valid Title
    [Arguments]   ${header_text}
    Location Should Be      ${DASHBOARD}
    Title Should Be    Dashboard 💀
    Element Should Contain   css:h1   ${header_text}
