# goit_python_core_hw_10

## test

### input

```
python main.py
Bot init
Enter your command:add
Sorry, there are not enough parameters or their value may be incorrect. Please use the help for more information.
Enter your command:
List of commands: hello, add, delete user, change phone, delete phone, show phone, show all, list, help, ?, good bye, close, exit, q, quit
Enter your command:add ?
Add user's phone or multiple phones separated by space. Required username and phone.
Enter your command:add Jon1 123 124 125
Done
Enter your command:list
Jon1, 123;124;125
Enter your command:delete
Can be: delete user, delete phone
Enter your command:delete phone ?
Delete user's phone. Required username, phone
Enter your command:delete phone Jon1 124
Done
Enter your command:list
Jon1, 123;125
Enter your command:delete phone Jon1 123
Done
Enter your command:list
Jon1, 125
Enter your command:delete phone Jon1 124
Sorry, there are not enough parameters or their value may be incorrect. Please use the help for more information.
Enter your command:delete phone Jon1 125
Done
Enter your command:list
Jon1,
Enter your command:add Jon1 123 124 125
Done
Enter your command:list
Jon1, 123;124;125
Enter your command:change
Can be: change phone
Enter your command:change phone Jon1 125 126
Done
Enter your command:list
Jon1, 123;124;126
Enter your command:list
Jon1, 123;124;126
Enter your command:?
List of commands: hello, add, delete user, change phone, delete phone, show phone, show all, list, help, ?, good bye, close, exit, q, quit
Enter your command:add Jon2 222
Done
Enter your command:list
Jon1, 123;124;126
Jon2, 222
Enter your command:show phone Jon1
123;124;126
Enter your command:show phone Jon2
222
Enter your command:delete ?
Help for this command 'delete ?' is not yet available
Enter your command:delete
Can be: delete user, delete phone
Enter your command:delete user ?
Delete ALL records of user. Required username.
Enter your command:delete user Jon1
Done
Enter your command:list
Jon2, 222
Enter your command:?
List of commands: hello, add, delete user, change phone, delete phone, show phone, show all, list, help, ?, good bye, close, exit, q, quit
Enter your command:q
Good bye
```
