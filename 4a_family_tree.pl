male(devidas).
male(kishan).
male(shrinivas).
male(anirudh).
male(kaustubh).
male(anish).
female(lalita).
female(sushama).
female(shweta).
female(prerana).
female(shreya).
female(sanvi).
child(shrinivas, lalita).
child(sushama, lalita).
child(anirudh, lalita).
child(kaustubh, sushama).
child(anish, sushama).
child(shreya, shweta).
child(sanvi, prerana).
wife(lalita, devidas).
wife(sushama, kishan).
wife(shweta, shrinivas).
wife(prerana, anirudh).

husband(X, Y):-wife(Y, X), male(X), female(Y).

mother(X, Y):-child(Y, X),female(X).

parent(X,Y):-(father(X, Y);mother(X, Y)).

father(X, Y):-husband(X, Z), mother(Z, Y).

grandparent(X,Y):-grandmother(X, Y);grandfather(X, Y).

grandmother(X, Y):-parent(Z, Y),mother(X, Z).

grandfather(X, Y):-parent(Z, Y),father(X, Z).

son(X, Y):-parent(Y, X),male(X).

daughter(X, Y):-parent(Y, X),female(X).

daughter_in_law(X, Z):-parent(Z,W),wife(X, W).

son_in_law(X, Z):-parent(Z,W),husband(X, W).

ancestor(X, Y):- parent(X, Y).
ancestor(X, Y):- parent(X, Z), ancestor(Z, Y).

successor(X, Y):- parent(Y, X).
successor(X, Y):- parent(Z, X), successor(Z, Y).

brother(X, Y):-child(X, Z),child(Y, Z),male(X),X\=Y.

sister(X, Y):-child(X, Z),child(Y, Z),female(X),X\=Y.

cousin(X,Y):-grandmother(P,X),grandmother(P,Y), \+brother(Y,X),X\=Y.

aunt(X, Y):-grandmother(Z, Y),(parent(Z, X) ; daughter_in_law(X, Z)),\+mother(X,Y),female(X).
uncle(X, Y):-grandfather(Z, Y),(parent(Z, X) ; son_in_law(X, Z)),\+father(X,Y),male(X).


/*
?- parent(X,anish).

X = kishan ;

X = sushama ;

No

?- grandparent(X,anish).

X = lalita ;

X = devidas ;

No

 ?- son(X, sushama).

X = kaustubh ;

X = anish ;

No

?- daughter(X, anirudh).

X = sanvi ;

No

?-brother(X, kaustubh).

X = anish ;

No

?- sister(sushama,Y).

Y = shrinivas ;

Y = anirudh ;

No

?-daughter_in_law(X, lalita).

X = shweta ;

X = prerana ;

No

?- son_in_law(X, lalita).

X = kishan ;

No

?- ancestor(X,anish).

X = kishan ;

X = sushama ;

X = devidas ;

X = lalita ;

No

?- successor(X, devidas).

X = shrinivas ;

X = sushama ;

X = anirudh ;

X = shreya ;

X = sanvi ;

X = kaustubh ;

X = anish ;

No

?- aunt(X,kaustubh).

X = shweta ;

X = prerana ;

No

uncle(X,kaustubh).

X = shrinivas ;

X = anirudh ;

No
*/