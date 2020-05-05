

def main():
    arr = [1,2,3,4,5,6,7,8,9]
    n = len(arr)
    count = 4
    newArray = [i for i in range(len(arr))]
    for i in range(n):
        newArray[ (i + n - count) %n] = arr[i]
        print(newArray[ (i + n - count) %n])
        print(arr[i])


    string = " ".join(map(str, newArray))

    print(string)

if __name__ == "__main__":
    main()
