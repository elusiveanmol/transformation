label startscene3:
    
    scene bg class_sciencelab
    with dissolve

    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_disco.mp3" loop

    show char anita at center
    an"Welcome to the Science wing of Durham University; more specifically, the Chemistry department."
    
    #play sound char_anita_throat
    
    an"I am Anita and Chemistry is my favorite course so I took this opportunity to be the tour guide for the Science Wing."
    an"As you can see, we have a lot of new equipment compared to other universities, like the {i}DNA samplers{/i}, {i}vial synthesizers{/i}, {i}centrifuges{/i} & of course the latest programmable {i}incubator{/i}."

    #show char_gale_funny
    #at left
    show char gale at left
    g"{b}Blah Blah Blah{/b} \(quietly)"
    
    #show char_leonard_laughing
    #at right
    show char leonard at right
    l"{b}hahahahaha!{/b}"
    
    #show char_anita_angry
    show char anita at center
    an"{b}{i}Ahem!{/i}{/b} You! You there with the squinty eyes. Are you mocking...{i}Science{/i}. How dare you!"
    
    #play sound char_anita_humph
    
    an"Humph!"
    ak"Whaaaaat!!!! No, it wasn't me! It was..."

    menu:
        "It was Leonard":
            jump anitablamesleonard

        "It was Gale":
            jump anitablamesgale

        "Cover for your friends and say it was you":
            jump anitablamesakira

        "Make an excuse and try to get away":
            jump excuseaway


label anitablamesleonard:
    
    stop music fadeout 0.5
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatsgoingon.mp3" loop

    #show char_leonard_shocked #at left
    show char leonard at left
    l"Dude, seriously! Thanks for being such a loyal bro!"
    
    #show char_anita_suspicious #at right
    show char anita at right
    an"I knew it! You insulting little..."

    g"Hey, hey, hey, cut it- Both of You!"

    ak"Gale is right, stop making a fool of yourselves. It was just a little joke."

    an"I knew you had a hand in this! Whatever your name is, {i}Mister{/i}. Your well-being & nourishment are all thanks to Science."

    l"It's {i}Leonard{/i} and look Anita, you are a smart girl. We were making fun of science because {i}we are stupid{/i}. Now forget about it. Okay?"

    an"All right, all right, all right. You proved your point. But I want to know who this new guy is?!"

    if playername == "My name is Akira":

        ak"Oh, I am Akira, I hail from Japan and I am here"
        
        if course == "Science":
            ak"for Science and beyond!"
            jump anitaright

        if course == "Languages":
            ak"{i}pour le{/i} Langues cours, {i}mademoiselle{/i}."
            jump anitaright

        if course == "Photography":
            ak"to attain creative nirvana in photography."
            jump anitaright

        if course == "Graphic Design":
            ak"to become a great {i}dribbbler{/i} at Graphic Design."
            jump anitaright

        if course == "Industrial Design":
            ak"in pursuit to change the world; one product at a time."
            jump anitaright

    
    if playername == "The name is Akira":

        ak"You can call me Akira. I am here"

        if course == "Science":
            ak"for the Science course."
            jump anitaright

        if course == "Languages":
            ak"precisely for the Languages course."
            jump anitaright

        if course == "Photography":
            ak"to become a photographer. I want to surpass someone. Badly."
            jump anitaright

        if course == "Graphic Design":
            ak"to achieve greatness in graphic design. It's tough road ahead but I am ready."
            jump anitaright

        if course == "Industrial Design":
            ak"to prove myself that I can be a great designer like {i}Shanz{/i}- my friend back in Japan."
            jump anitaright

label anitaright:

    ak"Anita, right? What got you into Chemistry? If you don't mind my asking."

    an"Umm, basically, it is something that I am good at and my family wanted me to become a scientist, so I chose {i}Chemistry{/i} as my main field of research."
    
    an"We can talk about this later, you have a tour to finish. Don't you?"

    g"Oh we sure do! Come on now, newbie!"
    with fade
    jump startscene4


label anitablamesgale:

    g"{b}What!{/b}. That is a complete lie! Leonard, help me out here, man!"

    an"Gale, I don't believe this! How could you? I have never made fun of your little toys."

    an"I {b}did not{/b} expect this from you Gale."

    stop music fadeout 0.5
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatjusthappened.mp3" loop

    g"Little toys!? {i}little toys!!!{/i} Those are real, intricate, lovingly-made products, okay!"

    ak"Anita, you just made fun of his career choice, it's equal now. Cool it both of you."

    l"Oh you are some one to {i}talk{/b} Akira."

    l"C'mon Gale, let's get out out here. Now we at least know who we should be careful around."

    #show char_leonard_stern
    show char leonard stern
    an"Wait! I am not done here. Who is this new guy tagging along with you?"
    ak"Oh! I am Akira! Not Squinty Eyes. I am from Japan and I am studying"

    if course == "Science":
            ak"Science."
            ak"We have to go now. Bye."
            with fade
            jump startscene4

    if course == "Languages":
            ak"the Languages."
            ak"We have to go now. Bye."
            with fade
            jump startscene4

    if course == "Photography":
            ak"Photography here."
            ak"We have to go now. Bye."
            with fade
            jump startscene4

    if course == "Graphic Design":
            ak"Graphic Design."
            ak"We have to go now. Bye."
            with fade
            jump startscene4

    if course == "Industrial Design":
            ak"industrial Design...just like Gale."
            ak"We have to go now. Bye."
            with fade
            jump startscene4


label anitablamesakira:

    ak"okay! Fine...it was me. Sorry!"
    #show char_anita_shocked
    show char anita
    
    an"..."
    
    #show char_leonard_shocked
    show char leonard
    l"A...Akira"
    
    ak"I shouldn't have laughed in the middle of your tour. It's just that my interest is"

    if course == "Science":
        ak"in Science and I was at awe with your love for chemistry."

    else:
        ak"not Science and the stuff that you were saying made no sense to me at all!"
    
    stop music fadeout 0.5
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_ceremony.mp3" loop

    #show char_anita_embarrassed
    show char anita
    an"Oh, is that so! Well, you should have told me earlier, then. No matter. Umm, what was your name again?"
    "I never mentioned her my name"

    ak"It's Akira."
    ak"Your name's Anita, right? What got you into Chemistry? If I may have the privilege to know."
    
    #show char_anita_happy
    show char anita
    an"Well Chemistry is something I am {b}really good{/b} at & I am doing this for my family. It seems odd but I don't mind studying this..."
    
    #show char_gale_upset
    show char gale
    g"Dude, let's go! Sorry to interrupt Anita but we have a tour to finish. I hope you understand!"
    
    #show char_anita_smile
    #with fade (0.5)
    show char anita with fade
    an"Oh sure, you guys carry on. I've got to work on something too."
    jump startscene4


label excuseaway:

    stop music fadeout 0.5
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatsgoingon.mp3" loop
    
    ak"Shit! That's my phone ringing, excuse me. I need to take this call!"
    
    #show char_anita_clever
    show char anita
    an"Nice try, smarty pants! But I am {b}not{/b} falling for that trick any time soon"
    ak"...Damn. It was an important call you know. What is it that you want?!"
    
    #show char_anita_upset
    show char anita
    an"What {b}I{/b} want? {i}You{/i} interrupted me and made fun of me. What I want...is an {u}explanation{/u}."
    ak"Look, I am Akira, and I am a new student here just like the rest of you people, studying"

    if course == "Science":
            ak"Science...just like you, Anita."

    if course == "Languages":
            ak"the Languages...just like Leonard."

    if course == "Photography":
            ak"Photography."

    if course == "Graphic Design":
            ak"Graphic Design."

    if course == "Industrial Design":
            ak"industrial Design...just like Gale."

    ak"Cut us some slack, okay. We were just having a bit of fun with your energetic introduction."
    
    #show char_anita_curious
    show char anita
    an"What's so funny about my energetic introduction? I was just stating the facts about our university's superior lab equipment."

    stop music fadeout 0.5
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_ceremony.mp3" loop

    ak"Oh no, we were not having a laugh because your intro was funny, we were having a laugh because your enthusiasm and the drive for chemistry {i}overwhelmed{/i} us."

    an"...,...,..."
    
    #play sound char_anita_throat
    
    an"Oh! I see."
    
    #show char_anita_embarrassed
    show char anita
    an"Well, I get carried away, sometimes. It's something I am trying to work on."
    ak"Anyways Anita, it was nice to meet someone who is so passionate about their line of work; a great tour by the way but we have to go and check out the other classes. Later!"
    with fade
    jump startscene4








