# Problem one
current_value = 0
save_current_value=0

if __name__== "__main__":
    print("Welcome to the calculator program")
    print("Current value: ", current_value, sep="")


# Problem two
def display_current_value():
    print("Current value: ", current_value, sep="")

if __name__== "__main__":
    display_current_value()


# Problem three
def add(to_add):
    global current_value
    current_value = current_value + to_add
    return current_value

if __name__== "__main__":
    display_current_value()
    print(add(5))
    display_current_value()


# Problem four
''' If we did not use "global current_value", the variable "current_value" in method "display_current_value()" and "add(to_add)" are not replated to each other. '''


# Problem five
def mult(to_mult):
    global current_value
    current_value = current_value * to_mult
    return current_value

if __name__== "__main__":
    display_current_value()
    print(mult(5))
    display_current_value()

def div(to_div):
    global current_value
    if to_div == 0: #divisor cannot be zero.
        return "You must be an artsci."
    else:
        current_value = current_value / to_div
        return current_value

if __name__== "__main__":
    display_current_value()
    print(div(0))
    display_current_value()


#Problem six:
def save():
    global current_value
    want_to_save = input("do you want to save this value? (Y or N):")
    if want_to_save == "Y":
        global save_current_value
        save_current_value = current_value
        print("Current value saved.")


def recall():
    global current_value
    want_to_recall = input("do you want to recall the stored value? (Y or N):")
    if want_to_recall == "Y":
        print("Your saved value is: " + str(save_current_value))


# Problem seven
current_value=0
previous_value=0

def display_current_value():
    print("Current value: ", current_value, sep="")

if __name__== "__main__":
    display_current_value()

def undo():
    global current_value
    global previous_value
    current_value, previous_value = previous_value, current_value
    display_current_value()

def add(to_add):
    global current_value
    global previous_value
    previous_value = current_value
    current_value = current_value + to_add
    return current_value

if __name__== "__main__":
    display_current_value()
    print(add(5))
    display_current_value()

def mult(to_mult):
    global current_value
    global previous_value
    previous_value = current_value
    current_value = current_value * to_mult
    return current_value

if __name__== "__main__":
    display_current_value()
    print(mult(5))
    display_current_value()

undo()
undo()
undo()