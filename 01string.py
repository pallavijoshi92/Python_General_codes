#numstring='100?00?1'
numstring=raw_input("Enter the string with 1,0 and ?:")
position=[]
for i in range(len(numstring)):
   if numstring[i]=='?':
        position.append(i)
print position    
numstring_list=list(numstring)
final=[]
for i in range(2**len(position)):
    s=list(bin(i)[2:].zfill(len(position)))
    for j in range(len(position)):
        numstring_list[position[j]]=s.pop()
    final.append(''.join(numstring_list))
print final 
    
        