import chatbot.addressbook as ab
from functools import wraps


def parse_input(command_line: str) -> tuple[str, list]:
    for command in COMMANDS:
        if command_line.lower().startswith(command):
            args = command_line.lstrip(command).strip().split(" ", 10)
            args = [s.strip() for s in args]
            return command, args
    return command_line.lower(), []


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Sorry, there are not enough parameters or their value may be incorrect. "\
                   "Please use the help for more information."
        except Exception as e:
            return "**** Exception other" + e
    return wrapper


@input_error
def handler_add(*args) -> str:
    user = args[0]
    args[1]
    phone = [ ab.Phone(p) for p in args[1:] ]
    if user in a_book:
        a_book.get_record(user).add_phone(phone)
    else:
        rec = ab.Record(ab.Name(user), phone)
        a_book.add_record(rec)
    return "Done"


@input_error
def handler_change_phone(*args) -> str:
    user = args[0]
    old_phone = args[1]
    new_phone = args[2]
    a_book.get_record(user).change_phone(ab.Phone(old_phone), ab.Phone(new_phone))
    return "Done"


@input_error
def handler_show_phone(*args) -> str:
    user = args[0]
    return a_book.get_record(user).get_phones()

@input_error
def handler_delete_phone(*args) -> str:
    user = args[0]
    phone = args[1]
    a_book.get_record(user).remove_phone(ab.Phone(phone))
    return "Done"    

@input_error
def handler_delete_record(*args) -> str:
    user = args[0]
    a_book.remove_record(user)
    return "Done"
    


def handler_show_all(*args) -> str:
    if any(a_book.keys()):
        return a_book
    else:
        return "No users found, maybe you want to add them first?"

def handler_show_csv(*args) -> str:
    if any(a_book.keys()):
        return a_book.get_csv()
    else:
        return "No users found, maybe you want to add them first?"


def handler_hello(*args) -> str:
    return "How can I help you?"


def handler_help(*args) -> str:
    command = " ".join(args)
    if not command:
        commands = list(COMMANDS.keys())
        commands.extend(COMMAND_EXIT)
        return "List of commands: " + ", ".join(commands)
    else:
        return COMMANDS_HELP.get(command,  f"Help for this command '{command}' is not yet available")


COMMAND_EXIT = ("good bye", "close", "exit", "q", "quit")

COMMANDS = {
    "hello": handler_hello,
    "add": handler_add,
    "delete user": handler_delete_record,
    "change phone": handler_change_phone,
    "delete phone": handler_delete_phone,
    "show phone": handler_show_phone,
    "show all": handler_show_all,
    "show csv": handler_show_csv,   
    "list": handler_show_all,
    "help": handler_help,
    "?": handler_help,
}

COMMANDS_HELP = {
    "hello": "Just hello",
    "add": "Add user's phone or multiple phones separated by space. Required username and phone.",
    "delete user": "Delete ALL records of user. Required username.",
    "delete": "Can be: delete user, delete phone",
    "change": "Can be: change phone",
    "change phone": "Change user's phone. Required username, old phone, new phone",
    "delete phone": "Delete user's phone. Required username, phone",
    "show": "Can be: show phone, show all",
    "show phone": "Show user's phones. Required username.",
    "show all": "Show all user's record.",
    "show csv": "Show all user's record in csv format",    
    "list": "Show all user's record.",   
    "help": "List of commands  and their description.",
    "?": "List of commands and their description. Also you can use '?' for any command as parameter",
    "exit": "Exit of bot.",
    "close": "Exit of bot.",
    "quit": "Exit of bot.",
    "q": "Exit of bot.",
    "good bye": "Exit of bot."
}

a_book = ab.AddressBook()


def main():
    print("Bot init")
    while True:
        try:
            user_input = input("Enter your command:")
        except KeyboardInterrupt:
            print("\r")
            break
        if user_input.lower() in COMMAND_EXIT:
            break
        else:
            command, args = parse_input(user_input)
            try:
                if len(args) == 1 and  args[0] == "?" :
                    result = COMMANDS['help'](command)
                else:
                    result = COMMANDS[command](*args)
            except (KeyError):
                result = COMMANDS['help'](command)
                print(result)
                # print("Your command is not recognized, try to enter other command. "
                #       "To get a list of all commands, you can use the 'help' command")
            else:
                if result:
                    print(result)
    print("Good bye")


if __name__ == "__main__":
    main()






# if __name__ == "__main__":
#     ab = AddressBook()
#     rec = Record(Name("Jon1"),[Phone("000-0001"),Phone("000-0002")],email=Email("bademail"))
#     rec.add_phone(Phone("000-0003"))
#     #rec.remove_phone("00-0001")
#     #print(rec)

#     ab.add_record(rec)
#     rec = Record("Jon2", ["200-0001", "200-0002"])
#     ab.add_record(rec)
#     rec = Record("Jon3", "300-0001", "Jon3@email.com")
#     ab.add_record(rec)

#     ab['Jon1'].remove_phone("000-0001")
#     ab['Jon1'].address.value="Jon1 Home Street"
#     ab['Jon2'].email.value = "Jon2@email.com"

#     for v in ab.values():
#         print( v)
