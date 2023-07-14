# add your code here
for i in range(1,101):
    is_by_three = i % 3 == 0
    is_by_five = i % 5 == 0
    if(is_by_three and is_by_five):
        print('FizzBuzz')
    elif(is_by_three):
        print('Fizz')
    elif(is_by_five):
        print('Buzz')
    else:
        print(str(i))
