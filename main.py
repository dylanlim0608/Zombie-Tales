

answer = input("Would you like to play (yes/no): ")
if answer.lower().strip() == "yes":
    answer = input("(It is a Saturday afternoon. Sunny skies, beautiful fresh air, and bird are chirping. You watch the new to stay inform on the shenanigance that occurs in the area. "
         "The reporter on the TV states that there is a national emergency occuring and authorities are advising everyone to bunker down in their homes. To you you think that "
         "what the reporter is saying is straight out of a movie. Suddenly, you see a person outside in your backyard. Just standing there) "
          "Do you check on him? (yes or no): ")
    if answer == "yes":
        answer = input("You walk up the man asking if he is ok. He turns around with his whole face full of blood and just making noise. Like he couldn't speak and only moan....like hes a zombie.....You stumble back in fear there is a brick and a shovel next to you what do you grab? (brick/shovel) : ")
        if answer.lower().strip() == "brick":
                 answer = input("You grab the brick. Gave the guy a good wack to the head. *BAM* The guy fell down and the brick shattered. Your hand hurts, you're covered in blood and now there is a dead guy in your backyard. As the adrenaline goes away slowly, you feel the pain more in your right hand. 'Its just bruised' you say to yourself. Shaking it off you check your phone to see if you can call someone. Anyone. There's one bar of service and you contemplate to either call your friend or your dad. Who do you call? (dad/friend):  ")

                 if answer.lower().strip() == "dad":
                     answer = input("You call your dad. No one else knows better than your dad. You trust your dad more than anything when it comes to advice and when you are in danger. Can't go wrong with family. He picks up in a panic but before he says anything you explain what just happened. You break down in tears because of a panic attack you are having. He calms you down and tells you 'Get here now! The world has gone to shit! Whatever you do, stay away from those crazy people. They'll try to bite you. I don't know what's happneing but just get here. Passcode to the gate is your birthday. Hurry and be safe.' He hangs up and the line goes dead. Listening to your father, you get ready to leave but thinks to yourself if you need to bring anything such as clothes, medicine, food, etc. or do you go with whatever you have on you? (pack/leave):  ")
                     if answer.lower().strip() == "pack":
                         answer = input("You decide to pack. You gather your things and realize you over packed. You forget your tons of clothes and only brough socks, underwear, spare pants, and some shirts. One jacket. Your favorite jacket. It's tough and has lots of pockets. It keeps you warm and comforts you. You keep it on as you leave with your stuff and make your way to your family's home. You get there no problem at all for some weird reason and arrive to the house. You enter the code, entering and closing the gate behind you. You haven't been here in years since you moved out. Your mother rushes out and hugs you. She looks very pale and there's blood on her shirt. Do you ask what happened or ignore it?(ask/ignore):   ")
                         if answer.lower().strip() == "ask":
                             answer = input("Mom...why is there blood on your shirt? Her smile went from worry-some mother to someone who lost everything. 'Our neighbor attacked me and tried to bite me. She was my best friend and I- I- I killed her!' Your mother cries more and you console her and tell her everything is ok. You enter the house and your dad is busy boarding up the house 'Hey get me that hammer and some extra nails! Hurry!' You help your dad board the windows up and only allows a half a foot gap to be able to see through. Do you peak? (yes/no)")
                             if answer.lower().strip() == "yes":
                                 answer = print("As you peak through, a crazed person reaches their hand through and gashes your eyes out. But the fingers on the hand was so long, it ended up impaling your brain as well resulting to death. YOU DIED [GAME OVER]")
                             elif answer.lower().strip() == "no":
                                 answer = print("You decided not to peak. You sit on the couch and decided to take a nap and sleep off the stress and confusion of what is happening. It felt like you were living a horror movie. You pass out, and when you wake up you're back in your own house with a movie on. Turns out it was a zombie movie you were watching and you fell asleep to it. Out of the corner of your eye, you see someone in your backyard....THE END [GAME OVER] ")
                             else:
                                 print("What you said or did or typed wasn't an option. You died. [GAME OVER]")
                         elif answer.lower().strip() == "ignore":
                             answer = print("Wow how incondierate to not ask your own mother what happened. You know what?....YOU LOST [GAME OVER]")
                         else:
                             print("What you said or did or typed wasn't an option. You died. [GAME OVER]")
                     elif answer.lower().strip() == "leave":
                         answer= print("Well you decide to leave. Not even prep yourself. Grown ass adult not even prepared for the worst. What can possibly go wrong? Well the worst happened. You tripped and fell and your head landed on a curb. YOU DIED [GAME OVER]")
                     else:
                         print("What you said or did or typed wasn't an option. You died. [GAME OVER]")

                 elif answer.lower().strip() == "friend":
                    answer = input("You call your friend Leon. He works for the police station and if anything goes wrong he can defend you. He's got a gun and probably extra one to spare. He picks up and you explain to him what you just did. 'Hey, its ok. You did what you had to do. It's crazy right now at the station. Officers are arresting these junkies psyched out on something and they keep trying to bite them.' You hear screaming in the background 'Shit. Mike! *BANG* We need an medical team here asap! Look I gotta go. I'll meet you at my place in 1 hour. Passcode to my door is my name. What the hell? I shot him! Why is he getting up still?! Mike what are you doing?!? Its me! *BANG BANG BANG*' The line goes dead....Confused you listen to your friend's advice and start heading to his house. However, you think that you should pack survival necessities but you also need to hurry up and get to Leon's house. What do you do? (pack/leave):  ")
                    if answer.lower().strip() == "pack":
                        answer = print("Being a rational adult, you decide to pack. You get your duffle bag and begin to pack. However due to studio budget, you were only allowed some clothing, a few supplies and a really expensive digital camera that was signed by famous new reporter Frank West. (Sorry) You hurry on over to Leon's house, enter the front gate, close it, and his girlfriend Ada has her gun pointed at you from the front door. 'Who are you? A news reporter trying to get the scoop of this chaos?' she says angrily at you. You explain everything that has happen and that some strange voice in your head told you to bring it. She rolls her eyes and lets you in. 'You got the BROKE REPORTER ending' [GAME OVER]")
                    elif answer.lower().strip() == "leave":
                        answer = print("As the irresponsible soul and degenerate of your family, you decided to just leave. You run to your friend's house and enter the front gate. Leon's girlfriend, Ada, has a gun pointed at you from the front door of the house. 'Care to explain who you are and why you are here' she says calmly. You explain the situation you're in and she lets you in the house. 'You got the IRRESPONSIBLE ADULT ending' [GAME OVER] ")
                    else:
                        print("What you said or did or typed wasn't an option. You died. [GAME OVER]")
                 else:
                    print("What you said or did or typed wasn't an option. You died. [GAME OVER]")
        elif answer.lower().strip() == "shovel":
                 answer = input("You grab the shovel and swung it at the thing's head. *CLANG* The guy falls down and now there is blood all over your shovel and Saturday outfit. 'Awe come on!' As you stand there realizing you just killed someone, your ears begin to ring and you start to tunnel vision. Do you black out? (yes/no): ")
                 if answer.lower().strip() == "yes":
                     answer = input("You pass out for a few hours. It is night time. You get up and see the body still lying in your backyard. You reach for your phone and realize you had service at some point and had 10 missed calls from your friends and family. There was a text from your dad that said 'Get over to the house ASAP!'. Another text from your friend saying the same. Who do you go to? (dad/friend):  ")

                     if answer.lower().strip() == "dad":
                         answer = input("You call your dad. No one else knows better than your dad. You trust your dad more than anything when it comes to advice and when you are in danger. Can't go wrong with family. He picks up in a panic but before he says anything you explain what just happened. You break down in tears because of a panic attack you are having. He calms you down and tells you 'Get here now! The world has gone to shit! Whatever you do, stay away from those crazy people. They'll try to bite you. I don't know what's happneing but just get here. Passcode to the gate is your birthday. Hurry and be safe.' He hangs up and the line goes dead. Listening to your father, you get ready to leave but thinks to yourself if you need to bring anything such as clothes, medicine, food, etc. or do you go with whatever you have on you? (pack/leave):  ")
                         if answer.lower().strip() == "pack":
                             answer = print("You decide to pack. You gather your things and realize you over packed. You forget your tons of clothes and only brough socks, underwear, spare pants, and some shirts. One jacket. Your favorite jacket. It's tough and has lots of pockets. It keeps you warm and comforts you. You keep it on as you leave with your stuff and make your way to your family's home. You get there no problem at all for some weird reason and arrive to the house. You enter the code, entering and closing the gate behind you. You haven't been here in years since you moved out. Your mother rushes out and hugs you. You enter the home and help your dad barricade the house. Standing guard to protect your family, you wait for rescue. 'You got the VANGUARD ending' [GAME OVER]  ")
                         elif answer.lower().strip() == "leave":
                             answer = print("Careless you just leave. Hauling ass to your family's home, you get to the gate, enter the code, open and close the gate, and run to the front door. Your mom sees you and runs to you. Crying you just hug her and cried. You enter the house with your mom and your dad barricaded the house. You then waited for rescue with your family...if it ever comes. 'You got the CRYBABY ending' [GAME OVER]")
                         else:
                                print("What you said or did or typed wasn't an option. You died. [GAME OVER]")

                     elif answer.lower().strip() == "friend":
                         answer = input("You call your friend Leon. He works for the police station and if anything goes wrong he can defend you. He's got a gun and probably extra one to spare. He picks up and you explain to him what you just did. 'Hey, its ok. You did what you had to do. It's crazy right now at the station. Officers are arresting these junkies psyched out on something and they keep trying to bite them.' You hear screaming in the background 'Shit. Mike! *BANG* We need an medical team here asap! Look I gotta go. I'll meet you at my place in 1 hour. Passcode to my door is my name. What the hell? I shot him! Why is he getting up still?! Mike what are you doing?!? Its me! *BANG BANG BANG*' The line goes dead....Confused you listen to your friend's advice and start heading to his house. However, you think that you should pack survival necessities but you also need to hurry up and get to Leon's house. What do you do? (pack/leave):  ")
                         if answer.lower().strip() == "pack":
                             answer = print("Confused, you put your phone away and begin to pack. As you pack, in the back of your head decided to throw in your favorite cast iron frying pan as one of the necessities. You say 'Hm this might come in handy.' You finish packing and kept it light but full. You leave and head over to Leon's place. As you make your way over, it's nothing but chaos. Cars are on fire, people are screaming, and for some strange reason you don't see anyone around. It's like its background noise to the horror to come. You reach Leon's place and enter the code. Entering and closing the gate behind you, his girlfriend Ada comes out with a gun pointed at your head from the front door. 'Who are you? Why are you here?' You respond 'Leon told me to come here and that he'll be here in an hour.' Looking cautious still she lets you in the house. 'You got the ZOMBIE GRITS ending' [GAME OVER]")
                         elif answer.lower().strip() == "leave":
                             answer = print("Careless and in a panic, you leave. Just left all your belongings at home. Didn't bring a single thing. Not even a cast iron frying pan. Werido. Anyway you run to Leon's, enter the code, open and closed the gate only to have his girlfriend, Ada pointing a gun at you. 'Why are you here and who are you?' She looked very calm and composed. You explain everything to her and she lets you in the house. 'You got the USELESS AND JUICELESS ending' [GAME OVER] ")
                         else:
                            print("What you said or did or typed wasn't an option. You died. [GAME OVER]")
                     else:
                         print("What you said or did or typed wasn't an option. You died. [GAME OVER]")

                 elif answer.lower().strip() == "no":
                     answer = input("You shake it off keeping your head together. You check your phone again for service...one bar. 'That's good enough for me' you say as you try to dial someone. You can call your dad who has a large house not too far from you that has a nice front gate or you can call your friend who is an officer and he lives the opposite direction from your family's home. Who do call? (dad/friends): ")
                     if answer.lower().strip() == "dad":
                         answer = input("You call your dad. No one else knows better than your dad. You trust your dad more than anything when it comes to advice and when you are in danger. Can't go wrong with family. He picks up in a panic but before he says anything you explain what just happened. You break down in tears because of a panic attack you are having. He calms you down and tells you 'Get here now! The world has gone to shit! Whatever you do, stay away from those crazy people. They'll try to bite you. I don't know what's happneing but just get here. Passcode to the gate is your birthday. Hurry and be safe.' He hangs up and the line goes dead. Listening to your father, you get ready to leave but thinks to yourself if you need to bring anything such as clothes, medicine, food, etc. or do you go with whatever you have on you? (pack/leave):  ")
                         if answer.lower().strip() == "pack":
                             answer = print("You decide to pack. You gather your things and realize you over packed. You forget your tons of clothes and only brough socks, underwear, spare pants, and some shirts. One jacket. Your favorite jacket. It's tough and has lots of pockets. It keeps you warm and comforts you. You keep it on as you leave with your stuff and make your way to your family's home. You get there no problem at all for some weird reason and arrive to the house. You enter the code, entering and closing the gate behind you. You haven't been here in years since you moved out. Your mother rushes out and hugs you. She looks very pale and there's blood on her shirt. Freaked out, you ran away and got eaten. 'You got the UNCOMPOSED ending' [GAME OVER] ")
                         elif answer.lower().strip() == "leave":
                             answer = print("Careless you just leave. Hauling ass to your family's home, you get to the gate, enter the code, open and close the gate, and run to the front door. Your mom sees you and runs to you. Crying you just hug her and cried. You and your mom enter the house both crying while your dad barricades the house. Onced barricaded, everyone in the house waits for rescue...if there is any. 'You got the HIDING CRYBABY ending. [GAME OVER]' ")
                         else:
                             print("What you said or did or typed wasn't an option. You died. [GAME OVER]")
                     elif answer.lower().strip() == "friend":
                         answer = input("You call your friend Leon. He works for the police station and if anything goes wrong he can defend you. He's got a gun and probably extra one to spare. He picks up and you explain to him what you just did. 'Hey, its ok. You did what you had to do. It's crazy right now at the station. Officers are arresting these junkies psyched out on something and they keep trying to bite them.' You hear screaming in the background 'Shit. Mike! *BANG* We need an medical team here asap! Look I gotta go. I'll meet you at my place in 1 hour. Passcode to my door is my name. What the hell? I shot him! Why is he getting up still?! Mike what are you doing?!? Its me! *BANG BANG BANG*' The line goes dead....Confused you listen to your friend's advice and start heading to his house. However, you think that you should pack survival necessities but you also need to hurry up and get to Leon's house. What do you do? (pack/leave):  ")
                         if answer.lower().strip() == "pack":
                             answer = print("Confused, you put your phone away and begin to pack. As you pack, in the back of your head decided to throw in your favorite cast iron frying pan as one of the necessities. You say 'Hm this might come in handy.' You finish packing and kept it light but full. You leave and head over to Leon's place. As you make your way over, it's nothing but chaos. Cars are on fire, people are screaming, and for some strange reason you don't see anyone around. It's like its background noise to the horror to come. You reach Leon's place and enter the code. Entering and closing the gate behind you, his girlfriend Ada comes out with a gun pointed at your head from the front door. 'Who are you? Why are you here?' You respond 'Leon told me to come here and that he'll be here in an hour.' Looking cautious still she lets you in the house. 'You got the PREPARED FOR THE WORST ending' [GAME OVER] ")
                         elif answer.lower().strip() == "leave":
                             answer = print("Careless and in a panic, you leave. Just left all your belongings at home. Didn't bring a single thing. Not even a cast iron frying pan. Werido. Anyway you run to Leon's, enter the code, open and closed the gate only to have his girlfriend, Ada pointing a gun at you. 'Why are you here and who are you?' She looked very calm and composed. You explain everything to her and she lets you in the house. 'You got the USELESS AND JUICELESS ending'[GAME OVER] ")
                         else:
                             print("What you said or did or typed wasn't an option. You died. [GAME OVER]")
                     else:
                         print("What you said or did or typed wasn't an option. You died. [GAME OVER]")
                 else:
                     print("What you said or did or typed wasn't an option. You died. [GAME OVER]")

        else:
            print("What you said or did or typed wasn't an option. You died. [GAME OVER]")

    elif answer =="no":
        print("You continue to watch TV. Next thing you know nothing happens. You live your life normally. THE END. 'You got the MIND YO DAMN BUSINESS ENDING' [GAME OVER]")
    else:
        print("What you said or did or typed wasn't an option. You died. [GAME OVER]")

elif answer.lower().strip() == "no":
    print("dang...ok [GAME OVER] ")

else:
    print("Uhhh that isn't apart of the script.....[GAME OVER]")
