import time

def readFile(FileName):
    file = open(FileName,"r")
    lines = file.readlines()
    file.close()
    return lines
    
def prepareValidData(FileName):
    lines = readFile(FileName)
    validLines = []

    for i in range(len(lines)):
        if ( len(lines[i]) >= 27000 and "N" not in lines[i][:27000]):
            validLines.append(lines[i][:27000])
    
    return validLines

def probes(fileName, probeLen): 
    
    genomeSequences = 27000 - (probeLen-1)
    myDic = dict()
    validData = prepareValidData(fileName)
    row_check = set()
        
    for i in range (len(validData)):
        row_check.clear()
        
        for j in range(genomeSequences):
            
            if( validData[i][j:j+probeLen] not in myDic.keys()):
                myDic[validData[i][j:j+probeLen]] = 1
                row_check.add(validData[i][j:j+probeLen])  
                
            elif( validData[i][j:j+probeLen] not in row_check ):
                myDic[validData[i][j:j+probeLen]] = myDic.get(validData[i][j:j+probeLen]) + 1
                row_check.add(validData[i][j:j+probeLen])
    
    return myDic,validData

if __name__ == '__main__':
    
    startTime = time.time()    
    myDic,validData = probes("turkey.txt",90)
    
    maxValue = max(myDic.values())
        
    count = 0
        
    nucleotides = []
        
    for key,value in myDic.items():
        if (value == maxValue):
            count += 1
            nucleotides.append(key)
    
    endTime = time.time()
    elapsedTime = endTime- startTime
    print(elapsedTime)
    
    open("NevzatBugrahanTurk.txt", "w")
    file = open("NevzatBugrahanTurk.txt", "w")
    
    file.write(str(len(validData)) +" "+ str(maxValue)+"\n")
    file.write(str(count)+'\n')
    file.write('\n'.join(nucleotides))
    file.close()

    