label startscene4:
    
    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatjusthappened.mp3" loop

    scene bg class_corridor
    with fade

    "Durham Corridors"

    #show char_leonard_smile
    show char leonard
    l"Hey Akira, we are gonna catch up with you later, Gale and I are going to his product lab to check out some new stuff he made. Go ahead for the next tour sans us, okay. Smell ya later!"

    scene bg class_creativeslab
    with fade

    "Creative Studio"

    ak"Wow. This is supposed to be the creative studio? Seems a bit desolated. Where is everybody. {b}Hello!{/b}."

    
    ##if tiinaboo == "Tiina Boo"

    #show silhoutte_char_tiina_smiling
    "Boo"
    with hpunch
    with vpunch

    ak"Nani!!!"
    jump tiinaheadache

##if you want to add a conditional such as this, remember that the $ var statement should come under a label not directly under a menu. Like so, label y: -> menu -> $ gift = "x". After this you can call the "if" statement successfully.

label tiinaheadache:

    if tiinaboo == "InvestigatetheNoise":
        menu:
            "What the fuck, Tiina!":
                jump wtftiina

            "Phew! Tiina, it's just you!":
                jump phewtiina

    if tiinaboo == "Backawayslowlyandreturntothedorm":

        menu:
            "What the fuck!":
                jump newwtf

            "Whose there!":
                jump newwhose

    if tiinaboo == "Headstraighttotheuniversitydorm,unpack&callitaday":
            
        menu:
            "What the fuck!":
                jump newwtf

            "Whose there!":
                jump newwhose


label wtftiina:
    
    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatsgoingon.mp3" loop

    ak"Are you out of your mind! You scared the hell out of me!"
    
    #show char_tiina_excited
    show char tiina at right
    t"Hahahahaha, ahahaha"
    
    #play char_tiina_humph
    
    t"Gotcha ya, Akira. Second time! That was good! You are here for the tour, I assume."
    t"And I happen to be in charge of this creative studio, so let's go!"
    jump endscene4

label phewtiina:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatsgoingon.mp3" loop

    ak"What were you thinking? Please don't do that again, okay?"
    
    #show char_tiina_disappointed
    show char tiina at left
    t"Awww, you are no fun at all! Not fair! I really wanted to get the drop on you like yesterday but I guess this try was an epic fail!"
    t"So, I take it that you are here for the tour? Let's begin, shall we?!"

label newwtf:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_recentdevelopment.mp3" loop

    ak"Who are you!? Are you out of your goddamn mind!"
    
    #show char_tiina_sad
    show char tiina at center
    t"Sorry, I am really sorry. I just though it might be a good idea to scare someone on their first day!"
    
    #show char_tiina_disappointed
    show char tiina
    t"This place is a bit quiet since the course hasn't started yet. I thought it would help pass the time and it was a bi boring since I am the tour guide for the creative studio"
    
    #show char_tiina_excited
    show char tiina
    t"Now, let me to show you around, okay?"
    jump endscene4

label newwhose:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_recentdevelopment.mp3" loop

    ak"Who might you be! Someone could have gotten hurt, you know!"
    
    #show char_tiina_stern
    show char tiina
    t"Oh, gimme a break, scardy cat! Nobody would get hurt by a silly prank like this."
    t"I just did that so I could avoid being bored from being a {i}tour guide{/i}. Oh wait! You are here for the tour, aren't you."
    #show char_tiina_excited
    show char tiina
    t"FINALLY!"
    t"C'mon, I will show you around... stay close, hahaha!"

    scene bg class_creativeslab
    with fade

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_disco.mp3" loop

    #show char_tiina_curious
    show char tiina
    t"So, you are the latest student to join Durham's aren't you. What's your name?"
    ak"Well, I go by the name of Akira, it means \"Graceful Strength\" in Japanese. What's yours?"

    #show char_tiina_happy
    show char tiina
    t"Oh, I am Tiina, the {i}overseer{/i} of the creative studio! I am studying the photography course here. I have always been drawn towards photography."
    
    #show char_tiina_smile
    show char tiina
    t"I try to see the beauty in all things and beings, irrespective of their actions and past. You? What are you studying here?"
    ak"Tiina, that's deep thinking, I wish I could see the beauty in everything but I guess I can be too judgmental sometimes."

    if course == "Science":
            ak"By the way, I am learning science. It's a very intriguing field to me and I feel that it can have a huge impact on our lives if it is explored in the right direction."
            jump endscene4

    elif course == "Languages":
            ak"By the way, I have chosen the Languages. It's a very intriguing field to me and I feel that it can have a huge impact on our lives if it is explored in the right direction."
            jump endscene4

    if course == "Photography":
            jump tiinaphotography

    elif course == "Graphic Design":
            ak"By the way, I have chosen graphic design. It's a very intriguing field to me and I feel that it can have a huge impact on our lives if it is explored in the right direction.to achieve greatness in graphic design. It's tough road ahead but I am ready."
            jump endscene4

    elif course == "Industrial Design":
            ak"By the way, I am practicing industrial design. It's a very intriguing field to me and I feel that it can have a huge impact on our lives if it is explored in the right direction."
            jump endscene4

label tiinaphotography:
    
    ak"Tiina...that's deep thinking. I have taken Photography, too! This is a pleasant surprise!"
    
    #show char_tiina_happy
    show char tiina
    t"It sure is, isn't it! I love shooting macros. It's amazing how nature has created such intricate details."
    
    #show char_tiina_smile
    show char tiina
    t"Macro photography, sometimes helps me remember that the beauty is within us and that we should just let it grow."
    t"Coming back to the tour..."
    jump endscene4

label endscene4:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_ceremony.mp3" loop

    #show char_tiina_curious
    show char tiina
    t"Check out the creative studio. It can support up to 20 students, is outfitted with Apple iMacs, lighting equipment for photo-shoots, a dark-room for film enthusiasts and a plethora of design books!"
    
    #show char_tiina_happy
    show char tiina
    t"The spacious desks give each student enough personal space to unleash their creative forces and harness them thorough the available resources."

    scene bg class_creativeslab:
    with fade

    show char tiina
    t"I sound like I'm in Sales!"
    
    #play sound char_tiina_giggle
    show char tiina
    t"but yeah, that concludes the tour of the studio. You should head back now & see if there are any other classes that still need to be checked out."
    t"Oh! Don't forget, the classes start tomorrow!"
    jump startscene5


