from maths import

print("hello,jacquesdavid!")
print("résoudre les equations du second degre")
print("ecrire les valeur a,b,c")
a = 1 
print(a)
b = 4
print(b)
c = 3
print(c) 
print("calculons le discriminant") 
d = b*b - 4*a*c 
print("d =", d)

print("calculer et affichons les solutions")
if d < 0 :
    print("l'équation n'admet pas de solution")
    if d == 0 :
        print("l'équation admet une solution double:", b/2*a)
        if d > 0 :
            print("l'équation admet admet deux solutions :", (-b-sqrt(d))/2*a, " et ", ( -b+sqrt(d))/2*a)