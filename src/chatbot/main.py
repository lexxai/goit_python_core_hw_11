from chatbot.address_book import AddressBook
from chatbot.fields import Name, Phone, Birthday, Email, Address
from chatbot.record import Record


from functools import wraps


def parse_input(command_line: str) -> tuple[ str, object, list ]:
    line:str = command_line.lower().lstrip()
    for command, commands in COMMANDS.items():
        for command_str in commands:
            if line.startswith(command_str):
                args = command_line[len(command_str):].strip().split()
                args = [s.strip() for s in args]
                return command_str, command, args
    return "undefined", handler_undefined, []


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
    phone = [ Phone(p) for p in args[1:] ]
    if user in a_book:
        a_book.get_record(user).add_phone(phone)
    else:
        rec = Record(Name(user), phone)
        a_book.add_record(rec)
    return "Done"


@input_error
def handler_change_phone(*args) -> str:
    user = args[0]
    old_phone = args[1]
    new_phone = args[2]
    a_book.get_record(user).change_phone(Phone(old_phone), Phone(new_phone))
    return "Done"


@input_error
def handler_show_phone(*args) -> str:
    user = args[0]
    return a_book.get_record(user).get_phones()

@input_error
def handler_delete_phone(*args) -> str:
    user = args[0]
    phone = args[1]
    a_book.get_record(user).remove_phone(Phone(phone))
    return "Done"    

@input_error
def handler_delete_record(*args) -> str:
    user = args[0]
    a_book.remove_record(user)
    return "Done"
    
def handler_show_all(*args) -> str:
    if a_book.len():
        return a_book
    else:
        return "No users found, maybe you want to add them first?"


@input_error
def handler_show_page(*args) -> str:
    if args[0]:
        a_book.max_records_per_page = int(args[0])
    try:
        page = next(a_book)
        return "\n".join([str(i) for i in page])
    except StopIteration:
        return "End list"               


def handler_show_csv(*args) -> str:
    if any(a_book.keys()):
        return a_book.get_csv()
    else:
        return "No users found, maybe you want to add them first?"


def handler_hello(*args) -> str:
    return "How can I help you?"


def handler_help( command:object = None ) -> str:
    if not command:
        commands = list( c for cs in COMMANDS.values() for c in list(cs) )
        return "List of commands: " + ", ".join(commands)
    else:
        return COMMANDS_HELP.get(command,  
               "Help for this command is not yet available")


@input_error
def handler_add_birthday(*args) -> str:
    user = args[0]
    birthday = args[1]
    a_book.get_record(user).add_birthday(Birthday(birthday))
    return "Done"

@input_error
def handler_add_email(*args) -> str:
    user = args[0]
    email = args[1]
    a_book.get_record(user).add_email(Email(email))
    return "Done"


@input_error
def handler_add_address(*args) -> str:
    user = args[0]
    address = " ".join(args[1:])
    a_book.get_record(user).add_address(Address(address))
    return "Done"


@input_error
def handler_delete_birthday(*args) -> str:
    user = args[0]
    a_book.get_record(user).delete_birthday()
    return "Done"


@input_error
def handler_delete_email(*args) -> str:
    user = args[0]
    a_book.get_record(user).delete_email()
    return "Done"


@input_error
def handler_delete_address(*args) -> str:
    user = args[0]
    a_book.get_record(user).delete_address()
    return "Done"


@input_error
def handler_days_to_birthday(*args) -> str:
    user = args[0]
    result = a_book.get_record(user).days_to_birthday()
    if result is None:
        result = f"No birthday is defined for user: {user} "
    elif result == 0:
        result = f"{result} days, Today is user {user}'s birthday !!!"
    else:
        result = f"{result} days"
    return result

@input_error
def handler_show_birthday(*args) -> str:
    user = args[0]
    result = a_book.get_record(user).birthday
    return result


@input_error
def handler_show_email(*args) -> str:
    user = args[0]
    result = a_book.get_record(user).email
    return result


@input_error
def handler_show_address(*args) -> str:
    user = args[0]
    result = a_book.get_record(user).address
    return result


def handler_exit(*args) -> str:
    return ""


def handler_undefined(*args) -> str:
    return handler_help()


def get_command_handler(command: str):
    for ch in COMMANDS:
        for cs in COMMANDS[ch]:
            if cs == command:
                return ch
    return handler_undefined


@input_error
def api(command: str, *args: list[str]) -> None:
    """API for run commands in batch mode

    Args:
        command (str): API command
        list[str]: API command arguments

    Returns:
        print API command result
    
    """
    result = get_command_handler(command)(*args)
    print(f"api command '{command}': {result}")



COMMANDS = {
    handler_hello: ("hello",),
    handler_delete_record: ("delete user", "-"),
    handler_change_phone: ("change phone",),
    handler_delete_phone: ("delete phone",),
    handler_show_phone: ("show phone",),
    handler_show_all: ("show all", "list", "l"),
    handler_show_page: ("show page",),
    handler_show_csv: ("show csv",),
    handler_help: ("help","?"),
    handler_add_birthday: ("add birthday",), 
    handler_delete_birthday: ("delete birthday",), 
    handler_add_email: ("add email",), 
    handler_delete_email: ("delete email",), 
    handler_add_address: ("add address",),
    handler_delete_address: ("delete address",),
    handler_days_to_birthday:  ("to birthday", ),
    handler_show_birthday: ("show birthday",),
    handler_show_email: ("show email",),
    handler_show_address: ("show address",),
    handler_add: ("add", "+"),
    handler_exit: ("good bye", "close", "exit", "q", "quit")
}


COMMANDS_HELP = {
    handler_hello: "Just hello",
    handler_delete_record: "Delete ALL records of user. Required username.",
    handler_change_phone: "Change user's phone. Required username, old phone, new phone",
    handler_delete_phone: "Delete user's phone. Required username, phone",
    handler_delete_email: "Delete user's email. Required username, email",
    handler_delete_address: "Delete user's address. Required username, address",
    handler_delete_birthday: "Delete user's birthday. Required username",
    handler_add_birthday: "Add or replace the user's birthday. Required username, birthday, "
                          "please use ISO 8601 date format",
    handler_add_email: "Add or replace the user's email. Required username, email",
    handler_add_address: "Add or replace the user's address. Required username, address",
    handler_show_phone: "Show user's phones. Required username.",
    handler_show_birthday: "Show user's birthday. Required username.",
    handler_show_email: "Show user's email. Required username.",
    handler_show_address: "Show user's address. Required username.",
    handler_show_all: "Show all user's record.",
    handler_show_page: "Show all user's record per page. Optional parameter size of page [10]",
    handler_show_csv: "Show all user's record in csv format",
    handler_days_to_birthday: "Show days until the user's birthday. Required username,",
    handler_add: "Add user's phone or multiple phones separated by space. "
                 "Required username and phone.",
    handler_help: "List of commands and their description. Also you can use '?' "
                  "for any command as parameter",
    handler_exit: "Exit of bot.",
    handler_undefined : "Command undefined"
}

a_book = AddressBook()


def main():
    print("\nChatBot initialized...\n")
    while True:
        try:
            user_input = input("Enter your command >>> ")
        except KeyboardInterrupt:
            print("\r")
            break
        
        command_str, command, args = parse_input(user_input)
        
        if len(args) == 1 and  args[0] == "?" :
            result = handler_help(command)
        else:
            result = command(*args)
        
        if result:
                print(result)

        if command == handler_exit:
            break



if __name__ == "__main__":
    main()

