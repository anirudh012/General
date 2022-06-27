import os, time, sys

total_indent = 10
current_indent = 0
indent_check = 1

try:
    while True:
        while indent_check == 1:
            print((' '*current_indent) + "###")
            current_indent += 1
            time.sleep(0.01)
            os.system('clear')
            if current_indent == total_indent:
                indent_check = 0
                break

        while indent_check == 0:
            print((' '*current_indent) + "###")
            current_indent -= 1
            time.sleep(0.01)
            os.system('clear')
            if current_indent == 0:
                indent_check = 1
                break

except KeyboardInterrupt:
    os.system('clear')
    print("Thank you for playing!")
    sys.exit()