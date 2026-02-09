def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    if check_answer(answer):
        print("yes")
    else:
        print("no")
#Checking answer and cases
def check_answer(a):
    if a == "42":
        return True
    elif a == "forty two":
        return True
    elif a == "forty-two":
        return True
    else:
        return False

#calling the function
main()

