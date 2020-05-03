#find median of two sorted arrays

def main():
    # list1 = [2,6,3,7]
    # list2 = [8,7,6,9]
    list1 = list(map(int ,input().rstrip().split()))
    list2 = list(map(int ,input().rstrip().split()))
    list1.sort()
    list2.sort()
    print(list1)
    print(list2)

    counterA = 0
    counterB = 0

    maxlen = len(list1)+len(list2)
    mainList = [" " for i in range(maxlen)]
    print(maxlen)

    for i in range(maxlen):
        if counterA < len(list1) and counterB< len(list2):
            if int(list1[counterA]) < int(list2[counterB]):
                mainList[i] = list1[counterA]
                counterA += 1
            else:
                mainList[i] = list2[counterB]
                counterB += 1
        elif counterA < len(list1):
            mainList[i] = list1[counterA]
            counterA += 1
        elif counterB < len(list2):
            mainList[i] = list2[counterB]
            counterB += 1

    if(maxlen % 2) != 0:
        result = mainList[int(maxlen/2)]
    else:
        result = (mainList[int(maxlen/2)-1] + mainList[int(maxlen/2)] )/2

    print(result)


if __name__ == "__main__":
    main()
