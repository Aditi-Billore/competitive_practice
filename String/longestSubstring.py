# find logest substring with non repeating words

def findSubString(testString):
    uniqueString = []
    isSpace = 0
    length = 0
    for let in testString:

        if let.isspace() and isSpace!= 0:
            length = length+1
            isSpace = 1

        if let not in uniqueString:
            uniqueString.append(let)
            length = len(uniqueString) if len(uniqueString)> length else length


        else:
            length = len(uniqueString) if len(uniqueString)> length else length
            while let in uniqueString:
                newIndex = uniqueString.index(let)
                uniqueString = uniqueString[newIndex+1: ]

            uniqueString.append(let)
    return length




def main():
    testString = input()
    length = findSubString(testString)
    print(length)

if __name__ == "__main__":
    main()
