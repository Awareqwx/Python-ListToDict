def zipLists(arr1, arr2):
    d = {}
    if len(arr1) >= len(arr2):
        for i in range(0, len(arr1)):
            if i < len(arr2):
                d[arr1[i]] = arr2[i]
            else:
                d[arr1[i]] = None
    else:
        for i in range(0, len(arr2)):
            if i < len(arr1):
                d[arr2[i]] = arr1[i]
            else:
                d[arr2[i]] = None
    return d

print zipLists(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])
print
print zipLists(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks"])
print
print zipLists(["Anna", "Eli", "Pariece", "Brendan", "Amy"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])