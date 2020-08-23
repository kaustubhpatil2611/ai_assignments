Rules:-
addition(X, Y):- Z is X + Y, write(Z),nl.
subtraction(X, Y):- Z is X - Y, write(Z),nl.
multiplication(X, Y):- Z is X * Y, write(Z),nl.
division(X, Y):- Z is X / Y, write(Z),nl.
modulus(X, Y):- Z is mod(X, Y), write(Z),nl.
power(X, Y):- Z is X**Y, write(Z),nl.
square(X):- Z is X**2, write(Z),nl.
square_root(X):- Z is X**0.5, write(Z),nl.
factorial(1, 1). 
factorial(X, Fact) :- X > 1,Y is X - 1,factorial(Y, W),Fact is W * X.

/*
?- addition(3,4).
7

?- subtraction(3,4).
-1

 ?- multiplication(20,4).
80

?- square(4).
16

?- division(20,4).
5

?- power(3,4).
81

 ?- square_root(4).
2

?- factorial(5,X).
X = 120 



*/