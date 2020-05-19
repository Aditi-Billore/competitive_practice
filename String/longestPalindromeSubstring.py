def checkPalindrome(str):
    # result = False
    # if len(str) > 1:
    #     for i in range(len(str)):
    #         if str[i] == str[len(str)-i-1]:
    #             result = True
    #             continue
    #         else:
    #             result = False
    #             break
    # return str if result else " "
    return str if str == str[::-1] else ""



def findPalindrome(str):
    temp = str
    start = 0
    maxNum = 0
    length = 0
    maxPali = " "
    while start < len(str):

        end = len(str)

        while end>start:
            pali = checkPalindrome(str[start:end])
            length = len(pali)
            if length > maxNum:
                maxNum = len
                maxPali = pali
            end -= 1

        start += 1



def main():
    str = input().rstrip()
    findPalindrome(str)

if __name__ == "__main__":
    main()
