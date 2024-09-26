# https://www.bill.com/learning/bank-identification-number
import argparse
import re 

BIN_REGEXES = {
    "Master": "(51|45)[0-9]{14}$",
    "Amex": "(34|37)[0-9]{14}$",
    "Diners": "36[0-9]{14}$",
    "Visa": "4[0-9]{15}$"
}

def check_bin(number):
    clean_number = number.replace(" ", "")
    clean_number = clean_number.replace("-", "")

    for regex in BIN_REGEXES:
        if re.findall(BIN_REGEXES[regex], clean_number):
            print(f"{clean_number} is {regex}")
            break

def main():
    parser = argparse.ArgumentParser('Bin checker')
    parser.add_argument('cc_number')

    args = parser.parse_args()

    check_bin(args.cc_number)

if __name__ == '__main__':
    main()