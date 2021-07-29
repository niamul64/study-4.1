male(somsher).
male(rahim).
male(abul).
male(roish).
male(nazmul).
male(niamul).
male(ziarul).
male(zaman).
male(manik).
male(shahin).
male(siam).
male(emon).
male(iqbal).
male(sobuj).
male(saair).

female(obiron).
female(nazma).
female(gibon).
female(sabina).
female(shara).
female(panna).
female(eva).
female(rina).
female(shumi).
female(nourin).

father(somsher,rahim).
father(somsher,abul).
father(somsher,roish).
father(rahim,niamul).
father(rahim,nazmul).
father(abul,panna).
father(abul,zaman).
father(roish,rina).
father(roish,shahin).
father(shahin,siam).
father(zaman,emon).
father(ziarul,nourin).
father(iqbal,sobuj).
father(nazmul,saair).

mother(obiron,rahim).
mother(obiron,abul).
mother(obiron,roish).
mother(nazma,niamul).
mother(nazma,nazmul).
mother(shara,saair).
mother(gibon,panna).
mother(gibon,zaman).
mother(eva,emon).
mother(sabina,rina).
mother(sabina,shahin).
mother(shumi,siam).








%rules




ancestor(X,Y):-
    father(X,Y) | father(X,Z),father(Z,Y).