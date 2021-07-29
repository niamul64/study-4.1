
%question2Anwser
parent(adam,betty).
parent(adam,charles).
parent(agatha,betty).
parent(agatha,charles).

parent(betty,david).
parent(ben,david).
parent(dawn,frank).
parent(david,frank).
parent(felicity,harry).
parent(frank,harry).

parent(charles,emma).
parent(charles,corinda).
parent(emma,george).
parent(edward,george).
parent(george,imogen).
parent(gwen,imogen).


%rules
grandparent(X,Z):-
    parent(X,Y),parent(Y,Z).

grandchild(X,Z):-
    grandparent(Z,X).


sibling(X,Z):-
    parent(Y,X),parent(Y,Z),Z\=X.

firstcousin(X,Y):-
    grandparent(Z,X),grandparent(Z,Y), not(sibling(X,Y)),Y\=X.

secondcousin(X,Y):-
    grandparent(A,X),grandparent(B,Y), not(sibling(X,Y)), sibling(A,B),X\=Y.



second_cousin_once_removed(X,Y):-
    secondcousin(X,Z),parent(Z,Y).



third_cousin(X,Y):-
    secondcousin(A,B),parent(A,X),parent(B,Y).