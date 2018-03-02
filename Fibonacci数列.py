f1=1
f2=1
for i in range(1,21):
        print(str.format("{0:32}{1:32}",f1,f2))
        if i%4==0:
                print(end=" ")
        f1+=f2
        f2+=f1

        
