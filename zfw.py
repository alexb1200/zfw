def inDict(dict,key):
    try:dict[key]
    except:return False
    return True

testStr=b"itty bitty spider went down the water spout. itty bitty spider went down the water spout. itty bitty spider went down the water spout."
intStr=[]
for c in testStr:
    intStr.append(c)

#print(testStr[0])
#print(dict["i"])


dict1 = {}
def compress(data):
        dict1 = {}
        for i in range(0, 255):
            dict1[chr(i)] = i


        code=255
        nuText=[]
        string=""
        for b in range(len(data)-1):
            string += chr(data[b])
            next = chr(data[b + 1])

            if not(inDict(dict1,string+next)):
                #print(string,"::::",dict[string]) #uncomment to see what string is assaoited with what code
                nuText.append(dict1[string])
                code+=1
                dict1[string+next]=code
                string=""
        nuText.append(dict1[next]) #grab the last char, the for loop doesnt pick it up because next looks ahead
        return nuText
def compressNum(data):
        dict1 = {}
        for i in range(0, 255):
            dict1[i] = i


        code=255
        nuText=[]
        string=""
        for b in range(len(data)-1):
            string += chr(data[b])
            next = chr(data[b + 1])

            if not(inDict(dict1,string+next)):
                #print(string,"::::",dict[string]) #uncomment to see what string is assaoited with what code
                nuText.append(dict1[string])
                code+=1
                dict1[string+next]=code
                string=""
        nuText.append(dict1[next]) #grab the last char, the for loop doesnt pick it up because next looks ahead
        return nuText



nuText= compress(testStr)
print(type(nuText))
print("Compressed Size:",len(nuText))
print("Original Size",len(testStr))

print("reduced by: ",(1- len(nuText)/len(testStr))*100,"%")


def decompress(data):
    #remaking the dictionary
    dict ={}
    for i in range(0,255):
        dict[i]=chr(i)

    #setup for decompression
    recoveredText=chr(data[0]) #grab first char
    char=""
    key=256
    NextCode=data[0]
    PrevCode=data[0]

    for b in range(len(nuText)-1):


        NextCode = data[b + 1]
        if(inDict(dict,NextCode)):
            string = dict[NextCode]

        else:
            string = dict[data[b]]
            string += char
        recoveredText += string
        #print(string, ":::",NextCode)

        #rebuilding the dictionary
        char=string[0]
        dict[key]=dict[PrevCode]+char
        key+=1
        #print(PrevCode,":::::",NextCode)
        PrevCode=NextCode
    return recoveredText
recoveredText=decompress(nuText)



print("\nrecovered text:")
print(recoveredText)

print("testing decomp on original:", len(decompress(testStr)))
apprStr = compress(testStr)
final=0
# for i in range(1000):
#
#
#
#     print("itr=",i," len= ",len(apprStr))
#     if len(apprStr) ==1:
#         final=i
#         break
#     if len(apprStr)==134:
#         print(apprStr)
#     temp=""
#     for num in apprStr:
#         temp+=chr(num)
#     apprStr=compress(temp.encode("utf-8"))


hypoStr=""
#for i in range(final):


apprStr = compress(testStr)
temp=""
for num in apprStr:
    temp+=chr(num)
apprStr=compress(apprStr)

v=decompress(apprStr)
temp=[]
for i in v:
    temp.append(ord(i))
v=decompress(temp)
print(v)







