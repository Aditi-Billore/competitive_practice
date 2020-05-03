# find index of two numbers from an array that add up to certain target value

def main():
    target = int(input("enter target value: "))
    nums = list(map(int, input().rstrip().split()))
    result = []
    indexA = -1
    indexB = -1
    for num in nums:

        indexA = indexA + 1
        if (target - num) in nums[indexA + 1: ]:

            indexB = nums[indexA+ 1: ].index(target - num)
            # to add indexB to original array value
            indexB = indexB+ indexA + 1
            if indexA != -1 and indexB != -1 and indexA != indexB:
                result.append(indexA)
                result.append(indexB)
                break


    print(result)


if __name__ == "__main__":
    main()
