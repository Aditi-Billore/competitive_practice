#find number of matcing strings in strings array

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    res = []
    for let in queries:
        res.append(strings.count(let))
    return res

if __name__ == '__main__':

    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'bc']
    res = matchingStrings(strings, queries)
    print(res)
