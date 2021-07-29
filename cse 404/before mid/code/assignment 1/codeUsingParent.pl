
parent(somsher,rahim).
parent(somsher,abul).
parent(somsher,roish).
parent(obiron,rahim).
parent(obiron,abul).
parent(obiron,roish).

parent(rahim,nazmul).
parent(rahim,niamul).
parent(nazma,niamul).
parent(nazma,nazmul).

parent(abul,panna).
parent(abul,zaman).
parent(gibon,panna).
parent(gibon,zaman).

parent(roish,rina).
parent(roish,shahin).
parent(sabina,rina).
parent(sabina,shahin).

parent(nazmul,saair).
parent(zaman,emon).
parent(shahin,simam).
parent(shara,saair).
parent(eva,emon).
parent(shumi,siam).

parent(panna,nourin).
parent(ziarul,nourin).

parent(nourin,sobuj).
parent(iqbal,sobuj).

%mother





%rules
grandparent(X,Z):-
    parent(X,Y),parent(Y,Z).
    %format("~w --> GrandParent of --> ~w",[X,Z]).
grandchild(X,Z):-
    grandparent(Z,X).
    %format("~w --> GrandChild of --> ~w",[X,Z]).

sibling(X,Z):-
    parent(Y,X),parent(Y,Z),Z\=X.
    %format("~w --> GrandChild of --> ~w",[X,Z]).

auntoruncle(X,W):-
    sibling(X,Y),parent(Y,W).
    %format("~w --> GrandChild of --> ~w",[X,Z]).

cousin(X,Y):-
    parent(Z,X),auntoruncle(Z,Y),X\=Y.
    %format("~w --> GrandChild of --> ~w",[X,Z]).

child(X,W):-
    parent(W,X).
    %format("~w --> GrandChild of --> ~w",[X,Z]).

firstcousin(X,Y):-
    grandparent(Z,X),grandparent(Z,Y), not(sibling(X,Y)),Y\=X.
    %format("~w --> first Cousin --> ~w",[X,Y]).
secondcousin(X,Y):-
    grandparent(A,X),grandparent(B,Y), not(sibling(X,Y)), sibling(A,B),X\=Y,
    format("~w --> Second Cousin --> ~w",[X,Y]).

   
thirdcousin(X,Y):-
    grandparent(A,X),grandparent(B,Y), cousin(A,B),X\=Y,
    format("~w --> third Cousin --> ~w",[X,Y]).

cousin_once_removed(X,Y):-
	firstcousin(X,Z), child(Y,Z),
    format("~w --> first cousin once removed --> ~w",[X,Y]).


cousin_twice_removed(X,Y):-
	firstcousin(X,Z), grandchild(Y,Z),
    format("~w --> first cousin twice removed --> ~w",[X,Y]).
    