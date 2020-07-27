
"""
def word_count(str):
    counts=dict()
    words=str.split()
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(word_count('the word thw words is the'))
"""
text=open("sample.txt","r")
d=dict()
for line in text:
    line= line.split()
    line =line.lower()
    words=line.split("")
for word in words:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
key in list(d.keys()) 
print(key,":",d[key])
        
