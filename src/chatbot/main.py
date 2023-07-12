from chatbot.address_book import AddressBook
from chatbot.fields import Name, Phone, Birthday
from chatbot.record import Record


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


def handler_help(*args) -> str:
    command = " ".join(args)
    if not command:
        commands = list(COMMANDS.keys())
        commands.extend(COMMAND_EXIT)
        return "List of commands: " + ", ".join(commands)
    else:
        return COMMANDS_HELP.get(command,  
               f"Help for this command '{command}' is not yet available")


@input_error
def handler_add_birthday(*args) -> str:
    user = args[0]
    birthday = args[1]
    a_book.get_record(user).add_birthday(Birthday(birthday))
    return "Done"


@input_error
def handler_delete_birthday(*args) -> str:
    user = args[0]
    a_book.get_record(user).delete_birthday()
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
def api(command: str, *args: list[str]) -> None:
    """API for run commands in batch mode

    Args:
        command (str): API command
        list[str]: API command arguments

    Returns:
        print API command result
    """
    result = COMMANDS[command](*args)
    print(f"api command '{command}': {result}")

COMMAND_EXIT = ("good bye", "close", "exit", "q", "quit")

COMMANDS = {
    "hello": handler_hello,
    "delete user": handler_delete_record,
    "change phone": handler_change_phone,
    "delete phone": handler_delete_phone,
    "show phone": handler_show_phone,
    "show all": handler_show_all,
    "show page": handler_show_page,
    "show csv": handler_show_csv, 
    "list": handler_show_all,
    "help": handler_help,
    "?": handler_help,
    "add birthday": handler_add_birthday,
    "delete birthday": handler_delete_birthday,
    "to birthday": handler_days_to_birthday,
    "show birthday": handler_show_birthday,
    "add": handler_add,
}

COMMANDS_HELP = {
    "hello": "Just hello",
    "delete user": "Delete ALL records of user. Required username.",
    "delete": "Can be: delete user, delete phone",
    "change phone": "Change user's phone. Required username, old phone, new phone",
    "delete phone": "Delete user's phone. Required username, phone",
    "change": "Can be: change phone",
    "add birthday": "Add or change the user's birthday. Required username, birthday, "  
                    "please use ISO 8601 date format",
    "delete birthday": "Delete user's birthday. Required username",
    "to birthday": "Show days until the user's birthday. Required username,",
    "show phone": "Show user's phones. Required username.",
    "show birthday": "Show user's birthday. Required username.",
    "show all": "Show all user's record.",
    "show page": "Show all user's record per page. Optional parameter size of page [10]",
    "show csv": "Show all user's record in csv format",    
    "show": "Can be: show phone, show birthday, show all",
    "add": "Add user's phone or multiple phones separated by space. "
            "Required username and phone.",
    "list": "Show all user's record.",   
    "help": "List of commands  and their description.",
    "?": "List of commands and their description. Also you can use '?' "
         "for any command as parameter",
    "exit": "Exit of bot.",
    "close": "Exit of bot.",
    "quit": "Exit of bot.",
    "q": "Exit of bot.",
    "good bye": "Exit of bot."
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

