def main():
    numx = 3
    numy = 1

    numxBin = bin(numx).replace("b","")
    numyBin = bin(numy).replace("b","")

    print(numxBin)
    print(numyBin)

    if len(numxBin) > len(numyBin):
        extra = len(numxBin) - len(numyBin)
        for i in range(extra):
            numyBin = '0' + numyBin
    print(numxBin)
    print(numyBin)


    if len(numyBin) > len(numxBin):
        extra = len(numyBin) - len(numxBin)
        for i in range(extra):
            numxBin = '0' + numxBin

    hammingDistance = 0
    for i in range(len(numxBin)):
        if numxBin[i] != numyBin[i]:
            hammingDistance += 1

    print(hammingDistance)
if __name__ == "__main__":
    main()
