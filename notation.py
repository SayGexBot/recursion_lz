def convert_to_base(num, to_base):
    if to_base < 2:
        return 'out of range'
    if to_base > 16:
        return 'out of range'
    n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_to_base(n // to_base, to_base) + alphabet[n % to_base]
    
def main():
    num = int(input('number: '))
    base = int(input('convert base to: '))
    print(convert_to_base(num, base))

if __name__ == "__main__":
    main()