import sys
sys.path.append('../src')

from chatbot import main as ChatBot

if __name__ == "__main__":
    ChatBot.api("add","Jon-00", "+38044333223", "3344")
    ChatBot.api("add birthday","Jon-00", "1988-02-17")
    ChatBot.api("add","Jon-01", "+38044333223", "3344")
    ChatBot.api("add","Jon-02", "+38044333223", "3344")  
    ChatBot.api("add","Jon-03", "+38044333223", "3344")
    ChatBot.api("add","Jon-04", "+38044333223", "3344")
    ChatBot.api("add","Jon-05", "+38044333223", "3344")
    ChatBot.api("add","Jon-06", "+38044333223", "3344")
    ChatBot.api("add","Jon-07", "+38044333223", "3344")
    ChatBot.api("add","Jon-08", "+38044333223", "3344")
    ChatBot.api("add","Jon-09", "+38044333223", "3344")
    ChatBot.api("add","Jon-10", "+38044333223", "3344")
    ChatBot.api("add","Jon-11", "+38044333223", "3344")
    ChatBot.api("add","Jon-12", "+38044333223", "3344")

    ChatBot.main()

