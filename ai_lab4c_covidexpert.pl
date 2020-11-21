/*This is covid expert program that generates a score out of 10 for the chances of you being affected by covid */

/*symptoms with a covid score*/
symptom(fever,3).
symptom(cough,2).
symptom(headache,2).
symptom(nausea,2).
symptom(breathing_problem,3).
symptom(cold,1).
symptom(throat_ache,3).
/*travel history*/
history(china).
history(usa).
history(italy).
history(south_africa).
history(brazil).
/*preexisting diseases*/
diseases(obesity).
diseases(diabetes).
diseases(asthama).
diseases(chronic_lung_disease).
/*covid zones along with the zone name and a covid score*/
zone(pune,red,3).
zone(mumbai,red,3).
zone(nagpur,red,3).
zone(latur,orange,2).
zone(nashik,red,3).
zone(aurangabad,red,3).
zone(ratnagiri,orange,2).
zone(parbhani,yellow,1).
zone(gadchiroli,green,0).
zone(sindhudurg,green,0).
zone(sangli,orange,2).

/*start of the program*/
test:-write('Hello! I am covid checker.'), nl,test1(0).

/*test1(0) initializes the test score to 0*/
/*add up the score for each disease and send to initial_score*/
test1(Z):-
    write('Please enter symptoms:'),
    read(S),
	symptom(S,X),
	Y is X+Z,
	write('Any more symptoms?(yes/no): '),
	read(Input),
	( Input=yes
    ->test1(Y)
    ; initial_score(Y)
    ).
 
/*from here in each predicate vaiable A carries the test score*/
/*pass score to predicate check_history depending upon the test1 score*/
initial_score(A):-
	(A >5 ->
        nl,check_history(3)
    ;   (A > 3 ->
            nl,check_history(2)
        ;	(A >1 ->
        		nl,check_history(1)
    		;	nl,check_history(0)
    		)
        )
    ).

/*pass score to predicate check_zone depending upon the travel hisory*/
check_history(A):-
	write('Do you have any travel history?(type country name / no): '),read(H),Z is A+2, 
	(history(H)
	-> check_zone(Z),nl
	; check_zone(A),nl
	).

/*pass score to predicate check_proffesion depending upon the Zone*/
check_zone(A):-
	write('Where do you live?: '),read(Z),
	zone(Z,X,Y),
	write('You are in '),write(X),write(' zone!!'),S is A+Y,nl,nl,
	check_proffession(S).

/*pass score to predicate check_disease depending upon the condition*/
check_proffession(A):-
	write('Are you a health worker?(yes/no): '),read(Z),
	(Z=yes
	-> write('Please Take care!'),nl,nl,S is A+2,check_disease(S)
	; write('Be safe at home and dont get out of house!'),nl,nl,check_disease(A)
	).

/*pass score to predicate check_spread depending upon if person has pre existing disease*/
check_disease(A):-
	write('Do you have any pre existing disease,if yes then which?: '),read(Z),
	(diseases(Z)
	-> write('Oh,take care! You are at slightly more risk'),S is A + 1,nl,nl,check_spread(S)
	; write('Good,you are safe'),nl,check_spread(A)
	).

/*pass score to predicate check_age depending upon the contact*/
check_spread(A):-
	write('Have you come in direct contact with a covid patient?: '),read(Z),
	(Z=yes
	-> write('You must get your test done!'),S is A + 5,nl,nl,check_age(S)
	; write('Good,you are safe'),nl,check_age(A)
	).

/*pass score to predicate check_out depending upon the age*/
check_age(A):-
	write('Is your age above 45 ?: '),read(Z),
	(Z=yes
	-> write('Oh,take care! You are at high risk'),S is A + 2,nl,nl,check_out(S)
	; write('Good,you are safe'),nl,check_out(A)
	).

/*pass score to predicate final_score depending upon time out of house*/
check_out(A):-
	write('Have you been out of your house,for how many minutes?(type 0 if not gone out): '),read(Z),
	(Z>30 ->
		nl,S is A + 2,nl,final_score(S)
		;(Z >15 ->
	        nl,S is A + 1,nl,final_score(S)
	    ;   nl,S is A + 0,nl,final_score(S)
	    )
	).

/*final score is calculated*/
final_score(A):-
	/*score calculated out of 22 scaled down to 10*/
	S is A/2.2,
	(S >6 ->
        nl,write('You are at High risk for COVID-19'),write(' with a score of '),write(S),write(' from 10'),nl,write('So please get yourself tested immediately and be in isolation!')
    ;   (S > 4 ->
            nl,write('You are at Medium risk for COVID-19'),write(' with a score of '),write(S),write(' from 10'),nl,write('So if you get more ill then get yourself tested!')
        ;   nl,write('You are at Low risk for COVID-19'),write(' with a score of '),write(S),write(' from 10'),nl,write('You are most likely safe !')
        )
    ).
