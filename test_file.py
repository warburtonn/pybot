***Variables***
# variable             card_number         date    cvv
@{credit_card}         4444555566661111    0119    123

***Test Cases ***                   amount              receiver_card
test1                               100                 @{credit_card}

*** Keywords ***
[Arguments]          @{card}
Input Card Number With FOR



----------------------
Another file.txt
Input Card Number with for
     [Arguments]         @{credit_card}
     Wait until element is visible    ${NEW_P2P_SENDER_CARD}
     ${card_mumber_1}=       Get slice from list     @{credit_card}[0]     0       15
        :FOR    ${Item}   IN    ${credit_card_1}
#         \      press key       ${NEW_P2P_SENDER_CARD}      ${card_mumber_1}
          \     input text      ${NEW_P2P_SENDER_CARD}       ${card_number_1}
