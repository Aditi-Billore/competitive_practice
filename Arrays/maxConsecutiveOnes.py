def main():
    list1 = [1,1,1,0,0,0,1,1,1,1,1]
    maxOne = 0
    oneCounter = 0
    for i in list1:
        if i == 1:
            oneCounter += 1
        else:
            maxOne = oneCounter if oneCounter>maxOne else maxOne
            oneCounter = 0

    maxOne = oneCounter if oneCounter>maxOne else maxOne

    print(maxOne)

if __name__ == "__main__":
    main()
