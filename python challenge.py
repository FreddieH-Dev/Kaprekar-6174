count = 0
total = 0
times = 0
number = 0

thisdict = {0 : 0}

for number in range(123,9876):
    num_array = [int(digit) for digit in str(number)] #splits the number into an array
    if len(num_array) == 3:
        num_array.insert(0,0) #pads a 3 digit number
    if len(set(num_array)) == 4: #checks for repeating numbers
        count = 0
        times = 0
        while count < 2:
            accending_num = sorted(num_array) #orders in accending and decending number
            decending_num = sorted(num_array,reverse = True)
            small_int = int(''.join(map(str, accending_num)))
            big_int = int(''.join(map(str, decending_num))) #joins it as int
            total = big_int - small_int
            times += 1 #counts how many iterations
            if total == 6174:
                count += 1
            num_array = [int(digit) for digit in str(total)]
        print(number,"took",times,"attempts")
        thisdict.update({number: times})
    else:
        print(number,"was skipped due to repeating numbers")
        number += 1
        
search = input("would you like to search for a value?:   ")
if search.lower() == "yes":
    enter = int(input("Enter number to find iterations:   "))
    print(thisdict[enter])

dictionary_state = input("would you like the dictionary to be ordered by number or iterations?:   ")
if dictionary_state == "iterations":
    x = 1
else:
    x = 0
dictionary = input(f"would you like the dictionary to be accending or decending in respect to the {dictionary_state}?:   ")
if dictionary.lower() == "accending":
    sorted_dict = dict(sorted(thisdict.items(), key=lambda item: item[x]))
    print(sorted_dict)
elif dictionary.lower() == "decending":
    sorted_dict = dict(sorted(thisdict.items(),reverse = True, key=lambda item: item[1]))
    print(sorted_dict)
