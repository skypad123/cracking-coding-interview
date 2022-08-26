#used sort to check if character appear before
def run(stringA : str) -> bool:
    usedChar = set() 
    for item in stringA:
        if item in usedChar: 
            return False
        else: 
            usedChar.add(item)
    return True


if __name__ == "__main__": 
    StringA = ""
    print(run(StringA))