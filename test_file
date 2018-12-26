***Variables***
# variable      card_number         date    cvv
@{card}         4444555566661111    0119    123
${card_part}

***Test Cases ***                   amount              receiver_card
test1                               100                 @{card}

*** Keywords ***
Input Card Number With FOR



----------------------
Another file.txt
Input Card Number With FOR
    [Arguments]         @{card}
        :FOR            ${card_part}    IN      @{credit_card}[0]
        Focus   ${FIELD_LOCATOR}
        Input text     ${FIELD_LOCATOR}     ${card_part}
