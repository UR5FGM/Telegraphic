def welcome():
    welcome = "WELCOME TO TELEGRAPHIC!"
    print(welcome.center(len(welcome) + 53, "*") + "\n")
    print(
        f'     Select test type:\n-"1": Singles (letters only);\n-"2": Singles (digits only);\n-"3": Singles (letters and digits);\n-"4": Singles (other characters);\n-"5": Groups (letters only);\n-"6": Groups (digits only);\n-"7": Groups (letters and digits);\n-"8": Groups (other characters);\n"9": Enter message;\n-"0": EXIT.\n'
        + "_" * 80
        + '"F7" - "F8": Adjust tone;\n"F9" - "F10": Adjust rate;\n"F1" - Help.'
    )
