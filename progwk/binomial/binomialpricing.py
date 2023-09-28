import numpy as np
def binomial_pricing(S0, u, d, n):
    Sn = np.zeros((n+1,n+1))
    Sn[0, 0] = S0

    for i in range(1,n+1):
        for j in range(i+1):
            Sn[i, j]= Sn[i-1,j]*u
            if j>0:
                Sn[i,j]=Sn[i-1,j-1]*d


    return Sn

def Vf_pricing(n,tree,k, optype):
    Vf=np.zeros(n+1)
    for i in range(0, n+1):
        if optype=="call":
            Vf[i]= max(tree[n,i]-k, 0)
        else:
            Vf[i]=max(k-tree[n,i], 0)
    return Vf


S0=8
u=2
d=0.5
n=4
k=10
optype= "call"
tree = binomial_pricing(S0, u, d, n)

for i in range(n+1):
    print("Time step {}: {}".format(i, tree[i, :i+1]))



Vf= Vf_pricing(n, tree, k, optype)

print("Option pricing: ", Vf)

