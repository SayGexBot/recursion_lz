def pascal_triangle(n, /):
    if n == 0:      # https://systechgroup.in/blog-pascal-triangle-in-python/
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        tr_p = pascal_triangle(n-1)
        for i in range(len(tr_p[-1])-1):
            new_row.append(tr_p[-1][i] + tr_p[-1][i+1])
        new_row += [1]
        tr_p.append(new_row)
        return tr_p

def main():
    num = int(input("number of rows: "))
    tr = pascal_triangle(num)
    for row in tr:
        print(row)

if __name__ == "__main__":
    main()