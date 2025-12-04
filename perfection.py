def is_perfect_number(num, /):
    def div(num, cd=1, dl=[]):
        if cd > num:
            dl.pop(-1)
            return dl
        if num % cd == 0:
            dl.append(cd) 
        return div(num, cd + 1, dl)
    if num == sum(div(num)):
        return True
    else:
        return False
    
def main():
    num = int(input('check number for perfection: '))
    print(is_perfect_number(num))

if __name__ == "__main__":
    main()