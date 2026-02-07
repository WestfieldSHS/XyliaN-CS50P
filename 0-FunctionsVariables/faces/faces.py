#define main
def main():
    user_input = input("Enter input: ")
    user_input = convert(user_input)
    print(user_input)
#implement convert string
def convert(str_input):
    answer = str_input.replace(':)', '🙂').replace(':(', '🙁')
    return answer
#call the funtion
main()