# goit_python_core_hw_11

## test

### input

```
python main.py
Bot init
Enter your command:?
List of commands: hello, delete user, change phone, delete phone, show phone, show all, show page, show csv, list, help, ?, add birthday, delete birthday, to birthday, show birthday, add, good bye, close, exit, q, quit
Enter your command:add birthday ?
Add or change the user's birthday. Required username, birthday, please use ISO 8601 date format
Enter your command:show csv
name,phone,email,address,birthday
Jon-00,38044333223;3344,None,None,1988-02-17
Jon-01,38044333223;3344,None,None,None
Jon-02,38044333223;3344,None,None,None
Jon-03,38044333223;3344,None,None,None
Jon-04,38044333223;3344,None,None,None
Jon-05,38044333223;3344,None,None,None
Jon-06,38044333223;3344,None,None,None
Jon-07,38044333223;3344,None,None,None
Jon-08,38044333223;3344,None,None,None
Jon-09,38044333223;3344,None,None,None
Jon-10,38044333223;3344,None,None,None
Jon-11,38044333223;3344,None,None,None
Jon-12,38044333223;3344,None,None,None
Enter your command:list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;3344
name: Jon-02, phones: 38044333223;3344
name: Jon-03, phones: 38044333223;3344
name: Jon-04, phones: 38044333223;3344
name: Jon-05, phones: 38044333223;3344
name: Jon-06, phones: 38044333223;3344
name: Jon-07, phones: 38044333223;3344
name: Jon-08, phones: 38044333223;3344
name: Jon-09, phones: 38044333223;3344
name: Jon-10, phones: 38044333223;3344
name: Jon-11, phones: 38044333223;3344
name: Jon-12, phones: 38044333223;3344
Enter your command:add birthday Jon-08 19990712
Done
Enter your command:list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;3344
name: Jon-02, phones: 38044333223;3344
name: Jon-03, phones: 38044333223;3344
name: Jon-04, phones: 38044333223;3344
name: Jon-05, phones: 38044333223;3344
name: Jon-06, phones: 38044333223;3344
name: Jon-07, phones: 38044333223;3344
name: Jon-08, phones: 38044333223;3344, birthday: 1999-07-12
name: Jon-09, phones: 38044333223;3344
name: Jon-10, phones: 38044333223;3344
name: Jon-11, phones: 38044333223;3344
name: Jon-12, phones: 38044333223;3344
Enter your command:add birthday Jon-06 2000.02.22
Sorry, there are not enough parameters or their value may be incorrect. Please use the help for more information.
Enter your command:add phone Jon-06 fffsfs
Sorry, there are not enough parameters or their value may be incorrect. Please use the help for more information.
Enter your command:show page ?
Show all user's record per page. Optional parameter size of page [10]
Enter your command:show page
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;3344
name: Jon-02, phones: 38044333223;3344
name: Jon-03, phones: 38044333223;3344
name: Jon-04, phones: 38044333223;3344
name: Jon-05, phones: 38044333223;3344
name: Jon-06, phones: 38044333223;3344
name: Jon-07, phones: 38044333223;3344
name: Jon-08, phones: 38044333223;3344, birthday: 1999-07-12
name: Jon-09, phones: 38044333223;3344
Enter your command:show page
name: Jon-10, phones: 38044333223;3344
name: Jon-11, phones: 38044333223;3344
name: Jon-12, phones: 38044333223;3344
Enter your command:show page
End list
Enter your command:to birthday Jon-08
0 days, Today is user Jon-08's birthday !!!
Enter your command:to birthday Jon-00
220 days
Enter your command:q
Good bye
```

## v.0.2.0

```
tests> python .\chatbot-test.py
api command 'add': Done
api command 'add birthday': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add': Done
api command 'add email': Done
api command 'add email': Done
api command 'add address': Done
api command 'add address': Done
api command 'add address': Done
api command 'add birthday': Done

ChatBot initialized...

Enter your command >>> lsit
Help for this command 'lsit' is not yet available
Enter your command >>> list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;33441
name: Jon-02, phones: 38044333223;33442, email: jon02@example.com, address: Vul. Vorota gate 02, office. 1221344, birthday: 1999-08-11
name: Jon-03, phones: 38044333223;33443
name: Jon-04, phones: 38044333223;33444
name: Jon-05, phones: 38044333223;33445, email: jon05@example.com, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: 38044333223;33446
name: Jon-07, phones: 38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: 38044333223;33448
name: Jon-09, phones: 38044333223;33449
name: Jon-10, phones: 38044333223;33450
name: Jon-11, phones: 38044333223;33451
name: Jon-12, phones: 38044333223;33452
Enter your command >>> list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;33441
name: Jon-02, phones: 38044333223;33442, email: jon02@example.com, address: Vul. Vorota gate 02, office. 1221344, birthday: 1999-08-11
name: Jon-03, phones: 38044333223;33443
name: Jon-04, phones: 38044333223;33444
name: Jon-05, phones: 38044333223;33445, email: jon05@example.com, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: 38044333223;33446
name: Jon-07, phones: 38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: 38044333223;33448
name: Jon-09, phones: 38044333223;33449
name: Jon-10, phones: 38044333223;33450
name: Jon-11, phones: 38044333223;33451
name: Jon-12, phones: 38044333223;33452
Enter your command >>> show csv
name,phone,email,address,birthday
Jon-00,38044333223;3344,None,None,1988-02-17
Jon-01,38044333223;33441,None,None,None
Jon-02,38044333223;33442,jon02@example.com,"Vul. Vorota gate 02, office. 1221344",1999-08-11
Jon-03,38044333223;33443,None,None,None
Jon-04,38044333223;33444,None,None,None
Jon-05,38044333223;33445,jon05@example.com,"Vul. Vorota gate 112, office. 2332",None
Jon-06,38044333223;33446,None,None,None
Jon-07,38044333223;33447,None,Vul. Vorota gate 122,None
Jon-08,38044333223;33448,None,None,None
Jon-09,38044333223;33449,None,None,None
Jon-10,38044333223;33450,None,None,None
Jon-11,38044333223;33451,None,None,None
Jon-12,38044333223;33452,None,None,None
Enter your command >>> ?
List of commands: hello, delete user, change phone, delete phone, show phone, show all, show page, show csv, list, help, ?, add birthday, delete birthday, add email, delete email, add address, delete address, to birthday, show birthday, show email, show address, add, good bye, close, exit, q, quit
Enter your command >>> delete birthday Jon-02
Done
Enter your command >>> list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;33441
name: Jon-02, phones: 38044333223;33442, email: jon02@example.com, address: Vul. Vorota gate 02, office. 1221344
name: Jon-03, phones: 38044333223;33443
name: Jon-04, phones: 38044333223;33444
name: Jon-05, phones: 38044333223;33445, email: jon05@example.com, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: 38044333223;33446
name: Jon-07, phones: 38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: 38044333223;33448
name: Jon-09, phones: 38044333223;33449
name: Jon-10, phones: 38044333223;33450
name: Jon-11, phones: 38044333223;33451
name: Jon-12, phones: 38044333223;33452
Enter your command >>> delete email Jon-02
Done
Enter your command >>> list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;33441
name: Jon-02, phones: 38044333223;33442, address: Vul. Vorota gate 02, office. 1221344
name: Jon-03, phones: 38044333223;33443
name: Jon-04, phones: 38044333223;33444
name: Jon-05, phones: 38044333223;33445, email: jon05@example.com, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: 38044333223;33446
name: Jon-07, phones: 38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: 38044333223;33448
name: Jon-09, phones: 38044333223;33449
name: Jon-10, phones: 38044333223;33450
name: Jon-11, phones: 38044333223;33451
name: Jon-12, phones: 38044333223;33452
Enter your command >>> delete birthday Jon-02
Done
Enter your command >>> list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;33441
name: Jon-02, phones: 38044333223;33442, address: Vul. Vorota gate 02, office. 1221344
name: Jon-03, phones: 38044333223;33443
name: Jon-04, phones: 38044333223;33444
name: Jon-05, phones: 38044333223;33445, email: jon05@example.com, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: 38044333223;33446
name: Jon-07, phones: 38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: 38044333223;33448
name: Jon-09, phones: 38044333223;33449
name: Jon-10, phones: 38044333223;33450
name: Jon-11, phones: 38044333223;33451
name: Jon-12, phones: 38044333223;33452
Enter your command >>> delete address Jon-02
Done
Enter your command >>> list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;33441
name: Jon-02, phones: 38044333223;33442
name: Jon-03, phones: 38044333223;33443
name: Jon-04, phones: 38044333223;33444
name: Jon-05, phones: 38044333223;33445, email: jon05@example.com, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: 38044333223;33446
name: Jon-07, phones: 38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: 38044333223;33448
name: Jon-09, phones: 38044333223;33449
name: Jon-10, phones: 38044333223;33450
name: Jon-11, phones: 38044333223;33451
name: Jon-12, phones: 38044333223;33452
Enter your command >>> add email Jon-05b jon05@example.aaa
Sorry, there are not enough parameters or their value may be incorrect. Please use the help for more information.
Enter your command >>> add email Jon-05 jon05@example.aaa
Done
Enter your command >>> list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;33441
name: Jon-02, phones: 38044333223;33442
name: Jon-03, phones: 38044333223;33443
name: Jon-04, phones: 38044333223;33444
name: Jon-05, phones: 38044333223;33445, email: jon05@example.aaa, address: Vul. Vorota gate 112, office. 2332
name: Jon-06, phones: 38044333223;33446
name: Jon-07, phones: 38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: 38044333223;33448
name: Jon-09, phones: 38044333223;33449
name: Jon-10, phones: 38044333223;33450
name: Jon-11, phones: 38044333223;33451
name: Jon-12, phones: 38044333223;33452
Enter your command >>> add address Jon-05 sdsds ddsds dsdsdsd dwqd qefdadwfcjj ykguey ife,  yegif yfg uiegfw
Done
Enter your command >>> list
name: Jon-00, phones: 38044333223;3344, birthday: 1988-02-17
name: Jon-01, phones: 38044333223;33441
name: Jon-02, phones: 38044333223;33442
name: Jon-03, phones: 38044333223;33443
name: Jon-04, phones: 38044333223;33444
name: Jon-05, phones: 38044333223;33445, email: jon05@example.aaa, address: sdsds ddsds dsdsdsd dwqd qefdadwfcjj ykguey ife,  yegif yfg uiegfw
name: Jon-06, phones: 38044333223;33446
name: Jon-07, phones: 38044333223;33447, address: Vul. Vorota gate 122
name: Jon-08, phones: 38044333223;33448
name: Jon-09, phones: 38044333223;33449
name: Jon-10, phones: 38044333223;33450
name: Jon-11, phones: 38044333223;33451
name: Jon-12, phones: 38044333223;33452
Enter your command >>> show csv
name,phone,email,address,birthday
Jon-00,38044333223;3344,None,None,1988-02-17
Jon-01,38044333223;33441,None,None,None
Jon-02,38044333223;33442,None,None,None
Jon-03,38044333223;33443,None,None,None
Jon-04,38044333223;33444,None,None,None
Jon-05,38044333223;33445,jon05@example.aaa,"sdsds ddsds dsdsdsd dwqd qefdadwfcjj ykguey ife,  yegif yfg uiegfw",None
Jon-06,38044333223;33446,None,None,None
Jon-07,38044333223;33447,None,Vul. Vorota gate 122,None
Jon-08,38044333223;33448,None,None,None
Jon-09,38044333223;33449,None,None,None
Jon-10,38044333223;33450,None,None,None
Jon-11,38044333223;33451,None,None,None
Jon-12,38044333223;33452,None,None,None
Enter your command >>> q
Good bye
```
