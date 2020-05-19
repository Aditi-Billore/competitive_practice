def main():
    list1 = [-2,-1,0,1,2]

    for i in range(len(list1)):
        list1[i] = list1[i]*list1[i]
    list1.sort()
    print(list1)
if __name__ == "__main__":
    main()
