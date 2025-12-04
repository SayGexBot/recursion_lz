def gcd(x , y):
    if x < 0:
        return 'insufficient input'
    if y < 0:
        return 'insufficient input'
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
def main():
    num1 = int(input("x:"))
    num2 = int(input("y:"))
    print("GCD =", gcd(num1, num2))

if __name__ == "__main__":
    main()
