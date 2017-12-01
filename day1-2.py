# helping an elf collect a star by finding the sum of all digits that match the next digit in the list.

print('hello, this is aoc day 1 captcha bot')
sequence = str(input('please enter your sequence now: '))

print('your input was: ' + sequence)

sum = 0
count = 1
offset = len(sequence) / 2
while count <= len(sequence):
    if (count + offset) > len(sequence):
        
        if int(sequence[count-1]) == int(sequence[count-offset-1]):
            print('digit halfway around matches')
            sum = sum + int(sequence[count-1])
        print('current: ' + str(sequence[count-1]))
        print('next: ' + str(sequence[count-offset-1]))
    else:
        if int(sequence[count-1]) == int(sequence[count+offset-1]):
            print('digit halfway around matches')
            sum = sum + int(sequence[count-1])
        print('current: ' + str(sequence[count-1]))
        print('next: ' + str(sequence[count+offset-1]))

    

    count = count + 1

print('the sum of the digits of your input is: ' + str(sum))


