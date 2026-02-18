def main():
    #ask user for input
    time = input('What time is it? ')
    #if statement
    if 7.00 <= convert(time) <= 8.00:
        print("It's breakfast time")
    elif 11.30 <= convert(time) <= 14.30:
        print("It's lunch time")
    elif 18.00 <= convert(time) <= 19.45:
        print("It's dinner time")
    else:
        return
    
#convert define
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    