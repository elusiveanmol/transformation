label startscene5:

    scene bg class_corridor
    with fade

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_newday.mp3" loop

    "Durham Corridors"

    ak"That went well! Now, what other classes do I need to check out for this tour to end?"
    ak"Hmm, just one- the {b}Products lab{/b}"
    ak"I should hurry. I don't want to keep Leonard and Gale waiting on me like that. Doesn't give a good impression."
    
    scene bg college_hallway
    with fade

    "Hallway"

    ak"These hallways are so wonderful. The arches must have been so difficult to build and integrate with the main building."
    ak"Now, where is the lab? I don't want to get lost here."

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatsgoingon.mp3" loop

    #show sihouette_char_brendan_stern
    "A Silhouette approaches you from behind, the arms reaching out to grab you."
    ak"All right, there it is! The product La..."
    
    #show sihouette_char_brendan_stern
    "AKIRA!"
    ak"Arghh!!!"
    ak"GIMME AN EFFIN' BREAK Tiina...wait."
    ak"Who are {b}{i}YOU?!{/i}{/b} What do you want from me!?"

    #show sihouette_char_brendan_stern
    #show char_brendan_stern
    show char brendan
    n"Hey look. I don't mean to scare you but there is something that has been bothering me. Have you noticed the way Leonard acts and talks. especially in front of guys?"
    n"I mean he is smart and handsome but don't you think he is, like, hiding something? He always seems in a rush as if there is something he needs to accomplish."
    n"Right?"

    menu:
        "Hmm, now that you have mentioned it":
            jump spyleonard

        "I am not into gossiping":
            jump verifyyourself

label spyleonard:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatdidjusthappen.mp3" loop

    ak"He does appear a bit weird & finicky but what exactly are you implying here?"
    ak"Besides, I don't even know you, why should I be talking to you about all this?"

    #show char_brendan_apologetic
    show char brendan
    n"Yes, you are absolutely right. How rude of me to just disturb you in between the tour. I offer my sincere apologies."
    b"I am Brendan Chang and I am a South Korean graphic design student. You?"
    ak"I am Akira, I am studying"

    
label bcourse:
    if course == "Science":
            ak"Science here."
            jump spyleonardconvo

    elif course == "Languages":
            ak"the languages here."
            jump spyleonardconvo

    if course == "Photography":
            ak"the art of photography here."
            jump spyleonardconvo

    elif course == "Graphic Design":
            ak"graphic design, as well."
            jump spyleonardconvo

    elif course == "Industrial Design":
            ak"the practice of industrial design."
            jump spyleonardconvo

label spyleonardconvo:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatdidjusthappen.mp3" loop

    ak"So look, I will admit, I have noticed some oddities in Leonard's behavior but that's what makes us {i}human{/i}, right? Brendan? I mean, nobody is the same."
    ak"And even though all of us are of the same species, we are individuals too, with our own respective personalities, traits and behaviors. I don't think there really is a big deal regarding this."

    #show char_brendan_excited
    show char brendan
    b"See, that's the thing, Akira. It is a big deal. look, I am doing a poster design and I am trying to implement the attributes of a few students of Durham's as a visual metaphor in my work."
    b"So I was hoping if you could help me out by getting to know Leonard a bit more and by keeping me informed about his character traits."
    
    #show char_brendan_happy
    show char brendan
    b"That way, I can make a kick-ass poster of him. I am planning to do the same for you and the others too. What do you say?"

    menu:

        "Yes, and you owe me a poster!":
            jump spyleonardsuccess

        "This just doesn't feel right to me":
            jump spyleonardfail

label spyleonardsuccess:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_ceremony.mp3" loop

    ak"Okay, done! I will find out what I can about Leonard and in exchange, you design a poster of mine too."
    
    #show char_brendan_excited
    show char brendan
    b"Now, that's what I am talking about. Time to go, later Akira!"
    jump startscene6

label spyleonardfail:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_newday.mp3" loop

    ak"Sorry but its not really my place to snoop into other's business. i hope your poster series turns out to be awesome though."
    
    #show char_brendan_disappointed
    show char brendan
    b"Well, bummer, I have to say, I am a bit disappointed in you. Yes, I hope that they don't suck. Thanks for your concern, Akira."
    jump startscene6

label verifyyourself:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_whatdidjusthappen.mp3" loop

    ak"I am sorry but is very intrusive of you. I don't even know you and what you are asking me is something that I find a bit uncomfortable."
    
    #show char_brendan_smile
    show char brendand
    n"You know what, you are absolutely right, this approach was quite rude of me, sincere apologies."
    b"I am Brendan and I am a South Korean learning graphic design."

    ak"A South Korean! Interesting, I am from Kyoto, Japan. I took admission at Durham's to study"
    jump courseb

label courseb:

    if course == "Science":
            ak"Science here."
            jump verifyyourselfconvo

    elif course == "Languages":
            ak"the languages here."
            jump verifyyourselfconvo

    if course == "Photography":
            ak"the art of photography here."
            jump verifyyourselfconvo

    elif course == "Graphic Design":
            ak"graphic design, as well."
            jump verifyyourselfconvo

    elif course == "Industrial Design":
            ak"the practice of industrial design."
            jump verifyyourselfconvo

label verifyyourselfconvo:

    ak"since this is quite a well known university. The placements the alumni get are just astounding!"
    ak"Coming back to your thoughts on Leonard...I do not find his behavior odd. Maybe a bit hyper-active but why are you bringing this up?"
    
    #show char_brendan_smile
    show char brendan
    b"You see, Akira, I am doing a poster design and I am trying to integrate the attributes of a few selected students of Durham as a visual metaphor in my work. So I was hoping if you could help me out by getting to know Leonard a bit more and by keeping me informed about his character and traits. That way, I can make a kick-ass poster of him. I am planning to do the same for you and the others, too. What do you say?"
    ak"Your interest in Leonard sounds sincere..."

    menu:
        "So, yes, I will help you":
            jump verifyyourselfsuccess

        "but, it doesn't feel right to me":
            jump verifyyourselffail

label verifyyourselfsuccess:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_ceremony.mp3" loop

    ak"Okay! I will try finding out what I can but I get a poster too."
    
    #show char_brendan_happy
    show char brendan
    b"Great! A poster of you too! All right then, later Akira!"
    jump startscene6

label verifyyourselffail:

    stop music fadeout 0.5
    play music "C:/Users/Rajat/Dropbox/Cloud/Transformation/Assets/Sound/transformation_music_newday.mp3" loop

    ak"No! I am not going to talk behind anybody's back. Sorry Brendan but I would advise you to the research on your own."
    
    #show char_brendan_disappointed
    show char brendan
    b"I am disappointed in you Akira, Later..."
    jump startscene6
