number = float(input('Write your number: '))
number_ii = float(input('Write your number: '))
operator = input('Enter your arithmetic operator [+, -, *, /, %]: ')

if operator == '+' :
    print(number+number_ii)

elif operator == '-' :
    print(number-number_ii)

elif operator == '*':
    print(number*number_ii)

elif operator == '/' :
    print(number/number_ii)

elif operator == '%' :
    print(number%number_ii)

else:
    print('Math Error!')

