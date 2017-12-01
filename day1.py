# helping an elf collect a star by finding the sum of all digits that match the next digit in the list.

print('hello, this is aoc day 1 captcha bot')
sequence = str(input('please enter your sequence now: '))

print('your input was: ' + sequence)

sum = 0
count = 0
while count <= len(sequence)-1:
    if count == len(sequence)-1:
        print('current: ' + str(sequence[count]))
        print('last: ' + str(sequence[count-1]))
        print('next: ' + str(sequence[0]))
    else:
        print('current: ' + str(sequence[count]))
        print('last: ' + str(sequence[count-1]))
        print('next: ' + str(sequence[count+1]))
    count = count + 1



print('the sum of the digits of your input is: ' + str(sum))
