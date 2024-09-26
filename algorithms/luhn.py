# https://www.geeksforgeeks.org/luhn-algorithm/

def checkLuhn(number):
    total = 0
    for idx, number in enumerate(account_number[::-1]):
        if idx % 2 == 1:
            new_number = int(number) * 2
            if new_number > 9:
                number_str = str(new_number)
                new_number = int(number_str[0]) + int(number_str[1])
            total += new_number
        else:
            total += int(number)

    if total % 10 == 0: 
        return True
    return False

account_number = "1101798278"
print(checkLuhn(account_number))