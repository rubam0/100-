dic={"name":"ruba","old":21,"gender":"female"}
if "name" in dic:
    print("yes")
print(len(dic))
dic["job"]="student"
print(dic)
dic.pop("name")
print(dic)
dic.popitem()
print(dic)
dic.clear()
print(dic)
del dic
