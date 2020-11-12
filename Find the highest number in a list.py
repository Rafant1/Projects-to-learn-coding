numbers = [-8, 42, 2, 33, 54, 68, 32, -2, -365, 61, 154, 132, 248, 64, 232, 302, 502, 1120, -5, 5555, -5555, 682, 6382]


#In this program the function look_for_the_heighest_numbers is looking for the heighest number in a list
#It is based on a simple loop in which the program compares sets and then compares the highest number with the next value from the list
#After every check, the index position of x or y gets +1 in order to compare the next value with the actual higher number
#In order to complete the program we had to take for consideration a situation when the last number in the list has the biggest value that the penultime value
#In this situation, the highest number variable can't adopt the value of the last index position because the while loop terminates itself before assigning
#the value of the last index position of the list to the variable the_heighest
#By cause of the situation, I wrote a series of if statements to check if the value of the last position of the index has the heighest value
#and if so, to print it as the highest number of the list.


#Edit!!! Looked for another soultions and now I know that we can write this functions using very few lines of coded with for loop
#However, I will leave this in my repository as a testimony of my coding trainings
def look_for_the_heighest_number(list):
    the_heighest = 0
    position1 = 0
    position2 = 1
    x = list[position1]
    y = list[position2]
    while list[len(list)-1] != x and list[len(list)-1] != y:

        if x > y:
            the_heighest = x
            y = list[position2 + 1]
            position2 += 1

        elif x < y:
            the_heighest = y
            x = list[position1 + 1]
            position1 += 1

        elif x == y:
            x = list[position1]
            y = list[position1 +1]


    if x == list[len(list)-1] and x > the_heighest:
        print(f"The highest number is {x}.")
    elif x == list[len(list)-1] and x < the_heighest:
        print(f"The highest number is {y}.")

    elif y == list[len(list)-1] and y > the_heighest:
        print(f"The highest number is {y}.")
    elif y == list[len(list)-1] and y < the_heighest:
        print(f"The highest number is {x}.")

def main(list):
    look_for_the_heighest_number(list)

main(input())