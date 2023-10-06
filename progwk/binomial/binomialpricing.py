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





import numpy as np

def binomial_option_price_recursive(price_tree, r, delta_t, K, option_type, i=0, j=0):
    if i == len(price_tree) - 1:
        if option_type == 'call':
            return max(0, price_tree[i, j] - K)
        elif option_type == 'put':
            return max(0, K - price_tree[i, j])
    else:
        option_price_up = binomial_option_price_recursive(price_tree, r, delta_t, K, option_type, i + 1, j)
        option_price_down = binomial_option_price_recursive(price_tree, r, delta_t, K, option_type, i + 1, j + 1)
        if option_type == 'call':
            return np.exp(-r * delta_t) * (p * option_price_up + (1 - p) * option_price_down)
        elif option_type == 'put':
            return np.exp(-r * delta_t) * (p * option_price_up + (1 - p) * option_price_down)


S0=8
u=2
d=0.5
n=4
k=10
p= 0.5
q=0.5
r=0.25
optype= "call"
tree = binomial_pricing(S0, u, d, n)

for i in range(n+1):
    print("Time step {}: {}".format(i, tree[i, :i+1]))



Vf= Vf_pricing(n, tree, k, optype)

print("Option pricing: ", Vf)

option_price= binomial_option_price_recursive(tree, r, n, k, optype)
print(option_price)



