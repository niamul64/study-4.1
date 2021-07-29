%KB %a
taller(shafa,rashik).
taller(rashik,prince).
taller(prince,iqbal).



%rules %b
rule_tall(X,Y):- 
    taller(X,Y); (taller(X,Z),taller(Z,Y)) ; (taller(X,Z),taller(Z,A),taller(A,Y)).
   