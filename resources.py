*** Settings ***
Documentation     A resource file with reusable keywords and variables.
Resource      %PATH_TO_RESOURCE_FILEs%

***Keyword***
Keyword_name_1
  [Arguments]   $/@{variables}
  keyword_function
  ...
  keyword_function
  
Keyword_name_2
  [Arguments]   $/@{variables}
  keyword_function
  ...
  keyword_function 
