c = " play Die With Smile"
l = c.lower().split(" ")
n=len(l)
song = ""
for i in range(2,n):
    song += str(l[i])+str(" ") 
print(song)