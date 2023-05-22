katz_deli = []

def line(line_list):
    string = "The line is currently:"
    if len(line_list) == 0:
        print("The line is currently empty.")
    else:
        for index, n in enumerate(line_list):
            string += f" {index + 1}. {n}"
        print(string)

def take_a_number(line_list, name):
    line_list.append(name)
    print(f"Welcome, {line_list[-1]}. You are number {len(line_list)} in line.")

def now_serving(line_list):
    if len(line_list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {line_list.pop(0)}.")