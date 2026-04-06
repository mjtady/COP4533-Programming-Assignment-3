from hvlcs import HighestValueCommonSubsequence

def main():
    with open('data/example.in', 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()] 
        
        if not lines:
            return

        k = int(lines[0])
        
        charValues = {}
        for i in range(1, k + 1):
            pair = lines[i].split()
            if len(pair) == 2:
                charValues[pair[0]] = int(pair[1])

        strA = lines[k + 1]
        strB = lines[k + 2]

        value, subsequence = HighestValueCommonSubsequence.maximumValue(strA, strB, charValues)
        print(value)
        print(subsequence)              

if __name__ == "__main__":
    main()