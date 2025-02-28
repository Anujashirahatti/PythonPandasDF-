import pandas as pd #mport pandas
names=["Anu","Niru","Raju"]
branch=["ECE","CSE","doctor"]
list_of_data=list(zip(names,branch))
names.append("pallu")
branch.append("BAMS")
list_of_data=list(zip(names,branch))
df=pd.DataFrame(list_of_data,columns=["names","branch"])
for n,b in list_of_data:
    print(n,b)
    
