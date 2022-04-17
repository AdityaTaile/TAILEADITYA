tableData=[['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]
listlens=[]
tour=0
lists={}
for m in tableData:
    total=0
    tour+=1
    for n in m:
        total+=len(n)
        lists["list:",tour]=total
    print("list",tour,total)

itemcount=list(lists.values())
sortedlen=(sorted(itemcount,reverse=True))
longest=sortedlen[0]

#print (lists['list:', 1])
#print (longest)


for m in range(len(tableData[0])):
    for n in range(len(tableData)):
        print (tableData[n][m],end=" ")
        n+=1
    print ("".rjust(lists['list:', 1],"-"))
    m+=1