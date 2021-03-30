def getPairs(sequence, num):
    pair = ""
    
    if "U" in sequence:
        return "Error RNA nucleobases found!"
    
    
    for x in range(int(num)):
        if "A" in sequence[x]:
            pair += "T"
        elif "G" in sequence[x]:
            pair += "C"
        elif "C" in sequence[x]:
            pair += "G"
        elif "T" in sequence[x]:
            pair += "A"
    return pair

numInputs = input()
lengthOfSeq = []
DNA = []

for y in range(int(numInputs)):
    for x in range(2):
        if x == 0:
            lengthOfSeq.append(input())
        else:
            DNA.append(input())

for x in range(len(DNA)):
    print(getPairs(DNA[x], lengthOfSeq[x]))
