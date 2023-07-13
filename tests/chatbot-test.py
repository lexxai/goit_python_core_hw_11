import sys
sys.path.append('../src')

from chatbot import main as ChatBot

if __name__ == "__main__":
    ChatBot.api("add","Jon-00", "+38044333223", "3344")
    ChatBot.api("add birthday","Jon-00", "1988-02-17")
    ChatBot.api("add","Jon-01", "+38044333223", "33441")
    ChatBot.api("add","Jon-02", "+38044333223", "33442")  
    ChatBot.api("add","Jon-03", "+38044333223", "33443")
    ChatBot.api("add","Jon-04", "+38044333223", "33444")
    ChatBot.api("add","Jon-05", "+38044333223", "33445")
    ChatBot.api("add","Jon-06", "+38044333223", "33446")
    ChatBot.api("add","Jon-07", "+38044333223", "33447")
    ChatBot.api("add","Jon-08", "+38044333223", "33448")
    ChatBot.api("add","Jon-09", "+38044333223", "33449")
    ChatBot.api("add","Jon-10", "+38044333223", "33450")
    ChatBot.api("add","Jon-11", "+38044333223", "33451")
    ChatBot.api("add","Jon-12", "+38044333223", "33452")
    ChatBot.api("add email", "Jon-05", "jon05@example.com")
    ChatBot.api("add email", "Jon-02", "jon02@example.com")
    ChatBot.api("add address", "Jon-02", "Vul. Vorota gate 02, office. 1221344")
    ChatBot.api("add address", "Jon-05", "Vul. Vorota gate 112, office. 2332")
    ChatBot.api("add address", "Jon-07", "Vul. Vorota gate 122")
    ChatBot.api("add birthday", "Jon-02", "1999-08-11")


    ChatBot.main()

