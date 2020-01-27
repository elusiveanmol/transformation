label startscene2:

        stop music fadeout 1.0
        play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_newday.mp3" loop

        scene bg room_front
        with dissolve

        ak"That was some sleep!"
        ak"I don't recall sleeping that well in a long time"
        ak"I should get ready in a jiffy but what should I wear for the first day?"
        
        menu:
            "Formal Attire":
                jump formalattire
                
            "Casual Attire":
                jump casualattire
            
label formalattire:
        ak"These would be appropriate. After all, it's the first day of the university!"
        jump briefing
        
label casualattire:
        ak"A casual outfit will do just fine. It's a university not a high school."
        jump briefing
        
label briefing:
    
    stop music fadeout 1.0
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_disco.mp3" loop
    
    scene bg class_languages
    with fade
    
    show char teacher
    
    tea"Welcome to the {b}Languages Wing{/b} of the university, there are {i}three{/i} more wings you need to cover to complete your college tour."

    show bg class_sciencelab
    with dissolve

    tea"-{b}the Science Wing{/b},"
        
    show bg class_creativeslab
    with dissolve

    tea"-{b}the Creative Studio{/b},"
        
    with dissolve
    tea"and"
        
    show bg class_productslab
    with dissolve
    
    tea"-{b}the Products lab{/b}"
       
        
    scene bg class_languages
    with fade

    #show char_teacher_excited
    show char teacher    
    tea"Okay students, let's begin our Intro class since it is the first day of the Durham Graduate Batch - {i}2013-2014{/i}"

    #show char_teacher_stern
    show char teacher at left
    tea"Each one of you should make earnest efforts to familiarize yourself with your peers; they are going to be your friends, enemies, rivals, lovers and supporters."
    tea"You have one year to learn something valuable from here and I suggest you give your best. That's it for now."

    stop music fadeout 1.0
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatsgoingon.mp3" loop
    
    show char leonard
    with fade    
    with vpunch
    with hpunch
    l"Well, this is a drag!"
    l"I came here to major in English not to {i}*familiarize*{/i} myself with others."

    show char leonard
    l"I guess, we just have to do what the Prof. said."

    show char leonard
    "I am Leonard, Leonard Crosby. You?" 
    
    menu:
        "My name is {i}Akira{/i}, I hail from Kyoto, Japan!":
            $ playername = "My name is Akira"   #if playername == "My name is Akira":
            jump nameisakira
            
        "The name is Akira & getting to know {b}{i}ME{/i}{/b} won't be a drag.":
            $ playername = "The name is Akira"  #if playername == "The name is Akira":
            jump thenameisakira

label nameisakira:

        #show char_gale_smile
        #with dissolve
        show char gale
        g"Oh! So you are from Japan!"
        g"I have always admired the precise and modernistic approach of designers like Tadao Ando and Kaoru Mende"
        g"- they inspired me to get into Durham's Industrial Design course. Which course are you in?"
        jump courses

label courses:
        menu:
            "Science":
                $ course = "Science" #if course == "Science":
                jump Science
        
            "Languages":
                $ course = "Languages" #if course == "Languages":
                jump Languages

            "Photography":
                $ course = "Photography" #if course == "Photography":
                jump Photography

            "Graphic Design":
                $ course = "Graphic Design" #if course == "Graphic Design":
                jump GraphicDesign

            "Industrial Design":
                $ course = "Industrial Design" #if course == "Industrial Design":
                jump IndustrialDesign 

label Science:
    
    stop music fadeout 1.0
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_recentdevelopment.mp3" loop

    #show bg bg_science_stuff
    ak"I took up Science!, I am not into design and stuff. Not my {i}thing{/i}"
    g"Ah! So we have a brainiac here, Leonard. it's nice meeting ya, by the way, Akira."
    jump endscene2

label Languages:
    
    stop music fadeout 1.0
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_recentdevelopment.mp3" loop

    #show bg bg_langauge_Stuff
    ak"Umm, sure, sure! I mean I don't know these designers. I'm more inclined towards the languages."
    g"It's cool, really. To each to his own, as the saying goes. Welcome to Durhams, Akira."
    jump endscene2

label Photography:

    stop music fadeout 1.0
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_recentevelopment.mp3" loop
    
    #show bg bg_photography_stuff
    ak"Oh, it's Photography! I love capturing moments. A notable photographer goes by the name of Koda, he, inspired me to just get on with this a long time ago."
    g"I feel what you are saying, truly. I photograph things too, it's essential to get the essence of something right. Which then, I apply to my creations."
    jump endscene2

label GraphicDesign:
    
    stop music fadeout 1.0
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_recentdevelopment.mp3" loop

    #show bg bg_graphicdesign_stuff
    ak"Wow! That {i}is{/i} impressive. I love design and that's the reason why I am in the Graphic Design course."
    g"And, you made the right choice. Designers, after all, have the power to influence the world."
    jump endscene2

label IndustrialDesign:
    
    stop music fadeout 1.0
    play music "/Users/elusiveanmol/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_recentdevelopment.mp3" loop

    #show bg bg_industrialdesign_stuff
    ak"{b}AWESOME!{/b} I didn't know these legends were your role model too! I have dedicated my life emulating these proficient designers and now my journey has brought me here as an industrial design student."
    ak"Gale, I think, you and I are going to be rivals!"
    g"You said it! We're {b}on!{/b}"
    jump endscene2

label thenameisakira:

    #show char_gale_smile
    #with dissolve
    show char gale
    g"Akira?! So you are from Japan then! Cool. Don't mind Leonard, he can be a bit cocky sometimes."
    g"Anyways, I have taken Industrial Design. What course have you taken?"
    ak"Well, since you asked so politely- I am studying"
    jump courses

label endscene2:

    #show bg bg_industrialdesign_stuff
    l"Phew, finally you two had your conversation!"

    stop music fadeout 5.0

    l"Now, let's get a {i}move{/i} {b}on{/b}. We don't want to miss the college tour, now do we?!"
    jump startscene3
