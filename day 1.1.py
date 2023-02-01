def vidhaydhar(x,y):
    if len(x)!=len(y):
        return False
    for i in range(len(x)):
        count=0
        if x.count(x[i])!=y.count(y[i]):
            return False
    return True
print(vidhaydhar("fool","poor"))
print(vidhaydhar("foal","poor"))
print(vidhaydhar("too","bar"))
print(vidhaydhar("toto","yaya"))
