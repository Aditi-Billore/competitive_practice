def main():
    list1 = [111,223,4554,5322,2443]
    evenDigitCount = 0

    for i in list1:
        # digitCount = 0
        # temp = i
        # while temp > 0:
        #     digitCount += 1
        #     temp = temp//10
        #
        # if digitCount %2 == 0:
        #     evenDigitCount += 1
        if (i>9 and i < 100) or (i>999 and i<10000):
            evenDigitCount+=1 

    print(evenDigitCount)

if __name__ == "__main__":
    main()
