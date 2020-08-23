/* knowledge base*/

/*tasks*/
activity(' sing,talk,think,write,read.').

task(sing,'Why this kolaveri kolaveri kolaveri deeeeee..... ').
task(talk,'I am currently talking. :)').
task(think,'I am currently thinking. :)').
task(write,'See i have wriiten this statement itself. :)').
task(read,'Yes i will do read your commands :)').

/*tellme tasks*/
tellme(joke,'what do we call a rose who wants to go to moon...> Gulab-ja-moon.. :)').
tellme(rhyme,'Eliza Eliza > yes papa... Eating RAM > no papa.... Telling lies > no papa....open your mouth > hahahaha(lots of memory).. :)').
tellme(story,'once there lived a man .... thats it :)').

/*facts for checking if the person is in positive or negative mood*/
positive(happy).
positive(nice).
positive(well).
positive(good).
positive(excited).
negative(bored).
negative(sad).
negative(unwell).
negative(stressed).
negative(depressed).
/*facts for checking if the person is giving positive or negative feedback for eliza*/
positivef(awesome).
positivef(amazing).
positivef(nice).
positivef(smart).
positivef(interesting).
negativef(boring).
negativef(irritating).
negativef(stupid).
negativef(frustating).


/*dynamic list for randomly slecting a response*/
:- dynamic confuse/1.
confuse(['Please speak again.','Ok,thats something new.', 'Oh I see.', 'Oh,I didnt knew it.']).

eliza:-
	write('Hello, I am Eliza.'),nl,nl,
	eliza_loop.

eliza_loop:-
	write('Eliza:-'),
	read(Input),
	reply(Input).

/*can you questions*/
reply([can,you,X | _ ]):-
    ( task(X,Y) /*check*/
    ->write( 'yes i can '),write(X),nl,nl/*if fact checked*/
    ,eliza_loop
    ; write('no i cannot '),write(X),nl,nl/*else*/
    ,eliza_loop
    ).

/*intro reply*/
reply([hello,i,am,Name | _ ]) :-
    write('Hello, '), write(Name), write('! Pleased to meet you.'),nl,nl,
    eliza_loop.

/* reply*/
reply([tell,me,a,X | _ ]):-
    ( tellme(X,Y)
    ->write(Y),nl,nl/*if fact checked*/
    ,eliza_loop
    ;write('Sorry, i cant tell a '),write(X),nl,nl/*else*/
    ,eliza_loop
    ).

/*perform tasks*/
reply([X | _]):-
    task(X,Y),write(Y),nl,nl,eliza_loop.

/*tell todays date*/
reply([tell,me,todays,date]) :-
    date(X),write(X),nl,nl,
    eliza_loop.

/*eliza's activities*/
reply([what,can,you,do | _ ]) :-
    write('I can '),activity(X),write(X),nl,nl,
    eliza_loop.

/*how are you reply*/
reply([how,are,you]) :-
    write('i am good, its nice talking to you.'),nl,
    write('How are you?'),nl,nl,
    eliza_loop.

/*reply to persons mood*/
reply([i,am,X | _ ]):-
    /*if positive mood*/
    (positive(X) ->
        write('Thats great that you are '),write(X),nl,nl,eliza_loop
        /*if negative mood*/
    ;   (negative(X) ->
            write('Oh, please dont feel yourself '),write(X),nl,nl,eliza_loop
            /*else if didnt understood*/
        ;   write('Oh i didnt knew it...'),nl,nl,eliza_loop
        )
    ).

/*reply to feedback*/
reply([you,are,X | _ ]):-
    /*if positive feedback*/
    (positivef(X) ->
        write('Thank you! You too are '),write(X),nl,nl,eliza_loop
        /*if negative feedback*/
    ;   (negativef(X) ->
            write('I am sorry for being a '),write(X),write(' chatbot'),nl,nl,eliza_loop
            /*else if didnt understood feedback*/
        ;   write('Oh i might be so...'),nl,nl,eliza_loop
        )
    ).

/*stop eliza*/
reply([bye | _ ]):-
    write('Felt nice talking to you!, Bye....').

/*random reply if didnt understand query*/
reply([ Y | _ ]) :-
    retract(confuse([ Next | Rest ])),
    append(Rest, [ Next ], NewExcuseList),
    asserta(confuse(NewExcuseList)),
    write(Next), nl,nl,
    eliza_loop.

/*reply if the query is not in brackets*/
reply(X):-
    write('please type your query in square brackets.'),nl,nl,
    eliza_loop.
