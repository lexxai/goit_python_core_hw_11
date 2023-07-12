import sys
sys.path.append('../src')

from chatbot import main

if __name__ == "__main__":
    main.COMMANDS["add"]("Jon1", "+38044333223", "3344")
    main.COMMANDS["add birthday"]("Jon1", "1988-02-17")
    main.main()

