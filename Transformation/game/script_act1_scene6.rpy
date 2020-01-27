label startscene6:

    scene bg class_productslab
    with fade

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_recentdevelopment.mp3" loop

    g"There you are! Akira welcome to the Product Lab. This right here is my crib."
    g"I work here day and night, only going to my dorm to get some shut-eye."

    #show char_gale_smile at left
    show char gale at left

    #show char_leonard_surprise at right
    show char leonard at right

    g"Hey yo Leonard! Why don't you show Akira some of the stuff I made recently."
    g"Akira, you should check out my work over there. Let me know if you find anything interesting and I'd be happy to explain the purpose and function of anything you see here."

    #show char_leonard_excited
    show char leonard
    l"About time you showed up, Akira! Where have you been? We assumed that you got lost with all the different wings and classrooms at Durham's! It's a relief. Hurry up now! Gale over there, by the corner.."
    l"He is tinkering at something, seems a bit busy although he did tell me that if you have any questions or if you wanted to inquire something, he wouldn't mind."

    #show char_leonard_happy
    show char leonard
    #scene bg_productslab_items
    l"Over here, Akira, allow me to show some of Gale's finest creations. He is a {i}master{/i} at producing artifacts of emotional value..."
    
    #hide char_leonard_happy
    #show char_leonard_surprised
    show char leonard
    #show img_productslab_glassornament_small at right
    #with fade
    ak"{b}Cool!{/b} (You point at a distance) What's over there! That shiny thing!!!"

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_ceremony.mp3" loop

    #hide char_leonard_surprised
    #show img_productslab_glassornament_big
    #show char_leonard_confused
    l"That's a glass ornament of some kind Seems to me that Gale has some attachment to it."
    jump galeobjectglassornament

label galeobjectglassornament:

    menu:

        "Ask Leonard about the ornament":
            $ leonard_favor += 1
            #$ leonardglassornament = "Ask Leonard about the ornament"  #if leonardglassornament == "Ask Leonard about the ornament":
            jump leonardornament

        "Ask Gale about the ornament":
            $ gale_favor += 1
            #$ galeglassornament = "Ask Gale about the ornament"  #if galeglassornament == "Ask Gale about the ornament":
            jump galeornament

label leonardornament:

    ak"Leonard, what exactly is this ornament? I get the attachment part, even I get attached to {i}things{/i}."

    #show char_leonard_stern
    show char leonard at right
    l"Well I don't see any reason to get attached to materials. I mean, we degrade, we get old and we die."

    l"I rather spend my time with someone who I can grow with; someone living, not inanimate like this object. And honestly, I have no clue what this particular thing is."
    
    #show char_leonard_confused
    show char leonard at center
    l"It looks very intricate but hardy considering the quality of glass, maybe it's {i}Sapphire{/i} but it could be ordinary glass too."
    ak"Show me more stuff of his!"
    
    #show char_leonard_stern
    show char leonard
    jump showmemorestuff

label galeornament:

    #hide char_leonard_confused
    show char leonard at left
    #show char_gale_smile
    show char gale
    g"This piece is what I call the Cornucopia- it's a glass structure made of {i}Sapphire{/i}-it's a bit expensive than, say {i}Fiber Glass{/i} but very, {i}very{/i} strong. Wait, do you even know what a Cornucopia is, Akira?"

    menu:

        "Oh yes, of course, who doesn't?!":
            $ gale_favor -= 1
            jump cornucopiaknown

        " Unfortunately, no, I don't":
            $ gale_favor += 1
            jump cornucopiaunkown

label cornucopiaknown:

    #show char_gale_suspicious
    show char gale
    g"Well, I am sure you do, Akira."
    
    #show char_leonard_excited at right
    show char leonard
    l"Hey, Akira, come over here, I've got something uber cool to show you!"
    jump showmemorestuff

label cornucopiaunkown:

    #show char_gale_excited
    show char gale
    g"That's okay, allow me. Cornucopia is a fictional device which the futurists and the technologists define as a device able to produce, and manufacture any material."
    
    #show char_gale_confident
    show char gale at right
    g"It is deemed as one of the possible solutions to end worldwide poverty."
    
    #show char_gale_smile
    show char gale
    g"I named this ornament, Cornucopia because it gives me hope that one day we, humans; would be at a mutual understanding with each other regarding every subject, taboo or not."
    
    #show char_leonard_bored at right
    show char leonard at right
    l"Oh, spare e those descriptions, Gale!"
    l"Akira!..."
    l"Hey! Come on, I have something cool to show you!"
    jump showmemorestuff

label showmemorestuff:

    #show img_productslab_bottle_small
    #with fade (0.5)

    ak"Is this...a bottle?"
    
    #show char_leonard_confident at left
    show char leonard at left
    l"Not just any other bottle. it's a {u}{i}smart{/i}{/u} bottl..."
    ak"Hahahahahaha; smart...bottle. {i}Sigh{/i}"
    
    #hide char_leonard_confident
    #show char_gale_smile
    show char gale
    l"Akira, it really is; well {i}advanced{/i}. it shows the current temperature of the liquid inside and the {i}ph{/i} level of the liquid! isn't that right, Gale?"
    jump galeobjectsmartbottle
    
label galeobjectsmartbottle:

    menu:

        "Why don't we move on":
            $ leonard_favor += 1
            #$ leonardsmartbottle = "Why don't we move on"  #if leonardsmartbottle == "Why don't we move on":
            jump leonardbottle

        "Seriously, Gale?!":
            $ gale_favor += 1
            #$ galesmartbottle = "Seriously, Gale?!"  #if galesmartbottle == "Seriously, Gale?!":
            jump galebottle

label leonardbottle:
    
    #hide char_gale_smile
    ak"Hey Leonard, let's move on, I bet there are other interesting stuff to see!"
    
    #show char_leonard_confused
    show char leonard
    l"You sure seem to be in a hurry. Okay then."
    
    #hide char_leonard_confused
    #show char_leonard_confident
    show char leonard
    l"There is this one last thing and it is a {i}beaautyyy{/i}! {b}Oomph!{/b}"
    jump galealuminumcar

label galebottle:

    #hide char_gale_smile
    #show img_productslab_bottle_small at left
    #with fade (0.5)
    #show char_gale_happy at right
    show char gale at right
    ak"Wow! Seriously, man!? I did not have a clue that such features could be implemented on a water bottle!"
    g"Umm, yeah! It was pretty difficult since I am not from an engineering background and it's just a prototype for now."
    
    #hide char_gale_happy
    #show char_leonard_smile at right
    show char leonard at right
    l"Hey Akira, check this thing out; it is a {i}beaautyyy{/i}! {b}Oomph!{/b}"
    jump galealuminumcar

label galealuminumcar:

    #hide show char_leonard_confused
    #show char_leonard_excited at left
    show char leonard at left
    l"TADA!"
    
    #show img_productslab_aluminumcar_small at right
    #with fade (0.5)
    ak"{b}Now {i}THAT{/i}{/b} is a car! Damn, I love the finish. I never expected Gale to be this good at it, Leonard."
    
    #show char_leonard_confident
    show char leonard
    l"Nobody did! He recently made this, says he has been working on this for quite some time to get it just right."
    jump galeobjectaluminumcar

label galeobjectaluminumcar:

    menu:

        "Very fascinating, let's check out some more stuff":
            $ leonard_favor += 1
            #$ leonardacar = "Very fascinating, let's check out some more stuff"  #if leonardcar == Very fascinating, let's check out some more stuff:
            jump leonardcarend

        "Is that true Gale! What's so special about this?!":
            $ gale_favor += 1
            #$ galecar = "Is that true Gale! What's so special about this?!"  #if galecar == "Is that true Gale! What's so special about this?!":
            jump galecarend

label leonardcarend:

    #show char_leonard_confident
    show char leonard
    #show char_leonard_disappointed
    show char leonard
    l"There isn't...any. This is it, at least what is on display here. let's talk to Gale about what to do next, okay?"
    jump galeintroend

label galecarend:

    #hide char_leonard_confident
    #show char_gale_excited at left
    show char gale at left
    #show img_productslab_aluminumcar_big at right
    #with fade (0.5)
    g"Okay, so it's made of aluminum, I sketched and designed it in SolidWorks and queued it to the University's #D industrial printer. Then it was just about adding billet aluminum and letting the printer do it's magic from the SolidWorks schematic."
    jump galeintroend

label galeintroend:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_disco.mp3" loop

    if gale_favor > leonard_favor:
        g"Well, you have seen most of the stuff, there are a few more back in my dorm but I can show you those maybe later."
        g"It's getting pretty late I should probably close the lab. Leonard, what about you?"
        
        #show char_leonard_tired at left
        show char leonard at left
        l"Well, I am heading back to the Languages Wing. I need to submit the tour feedback. What about you two?"
        g"I am gonna go head to the dorm, kick back and chill. What about you Akira?"
        ak"I think I'm heading to the dorm as well. Today was a bit exhausting. With the jetlag and all the stress of moving into a new country."
        l"Well, it sure must be!"
        g"I feel ya. It took me 8 hours from the States!"
        l"However you arrived here a few days earlier than us, so you seem to have recovered. I am still burned out but I'm going to lay back as soon as I get done with this feedback. See ya!"
        g"You too, Akira!"
        ak"Later, fellas!"
        "Le Fin. Sshh! Act 2 is under development."
        scene black
        with Pause(0.5)

        show bg credits with dissolve
        with Pause(10)
        return

    elif leonard_favor > gale_favor:
        l"Phew, I am not cut out to be an orator. Haha! Hmm."
        g"Yeah, right...what do you both want to do now?"
        l"Well, I am heading back to the Languages Wing. I need to submit the tour feedback. What about you two?"
        g"I am gonna go head to the dorm, kick back and chill. What about you Akira?"
        ak"I think I'm heading to the dorm too. Today was a bit exhausting. With the jet lag and all the stress of moving into a new country."
        ak"Later, fellas!"
        "Le Fin. Sshh! Act 2 is under development."
        scene black
        with Pause(0.5)

        show bg credits with dissolve
        with Pause(10)
        return



