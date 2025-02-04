from calcul_on_Fq import extended_euclid_rec

for i in range(126):
    if (i**63)%127 == 1 :
        print(i)

u, v = extended_euclid_rec(2, 63)
print(u,v)