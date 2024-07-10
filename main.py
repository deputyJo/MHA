import random


class Character:
    def __init__(self, name, interactions, thoughts):
        self.name = name
        self.interactions = interactions
        self.thoughts = thoughts
        self.encounter_count = 0

    def interact(self):
        self.encounter_count += 1
        interaction = random.choice(self.interactions)
        return interaction

    def get_thoughts(self):
        return random.choice(self.thoughts)


# Define the characters and their interactions
characters = [
    Character("Kyoka", [
        "Kyoka sits on your face, pressing her weight down and laughing. She wiggles her toes against your nose, enjoying your discomfort.",
        "Kyoka pushes her stinky feet onto your face, smirking as you struggle to breathe. 'You like that, don't you?' she mocks.",
        "Kyoka grinds her feet on your nose, her laughter ringing in your ears. 'You make a good footrest,' she says.",
        "Kyoka mocks you as she sits on your face, her feet dominating your senses. 'You'll get used to it,' she laughs."
    ], [
                  "Kyoka thinks you're a pathetic loser.",
                  "Kyoka finds your face comfortable to sit on.",
                  "Kyoka enjoys making you suffer under her feet.",
                  "Kyoka thinks you deserve to be her footrest."
              ]),
    Character("Ochako", [
        "Ochako asks you to rub her feet, giggling as you nervously comply. 'Don't be shy, I know you love it,' she teases.",
        "Ochako demands a foot massage, her feet already sweaty from her training. 'Come on, put some effort into it!' she orders.",
        "Ochako makes you smell her sweaty feet, laughing at your expression. 'Isn't it wonderful?' she asks mockingly.",
        "Ochako laughs as you rub her feet, clearly enjoying your submission. 'You're pretty good at this,' she admits."
    ], [
                  "Ochako thinks you're a loser for enjoying this.",
                  "Ochako appreciates the effort you put into rubbing her feet.",
                  "Ochako enjoys watching you squirm.",
                  "Ochako thinks you have potential as a foot slave."
              ]),
    Character("Momo", [
        "Momo makes you lick her feet, her eyes glinting with amusement. 'I hope you like the taste,' she says with a smirk.",
        "Momo forces your tongue between her toes, enjoying your discomfort. 'Make sure to clean thoroughly,' she commands.",
        "Momo laughs as you lick her dirty feet, clearly relishing your humiliation. 'You're doing a great job,' she mocks.",
        "Momo commands you to clean her feet with your tongue, watching you closely. 'Don't miss a spot,' she warns."
    ], [
                  "Momo thinks you're beneath her.",
                  "Momo enjoys the feeling of your tongue on her feet.",
                  "Momo thinks you're a natural at this.",
                  "Momo finds it amusing to see you degrade yourself."
              ]),
    Character("Himiko", [
        "Himiko deepthroats you with her feet, laughing as you gag. 'Don't you just love my feet?' she teases.",
        "Himiko shoves her foot into your mouth, watching your reaction with glee. 'You better get used to this,' she says.",
        "Himiko enjoys making you gag on her feet, her laughter filling the room. 'You're so much fun to play with,' she giggles.",
        "Himiko forces her toes deep into your throat, relishing your struggle. 'You're mine now,' she declares."
    ], [
                  "Himiko thinks you're fun to play with.",
                  "Himiko loves watching you gag.",
                  "Himiko thinks you're the perfect toy.",
                  "Himiko enjoys your suffering."
              ]),
    Character("Mina", [
        "Mina tramples you with her feet, her laughter echoing in the room. 'You make a great mat,' she jokes.",
        "Mina steps on you repeatedly, enjoying your groans. 'This is a good workout,' she says cheerfully.",
        "Mina dances on your body, her feet pressing into you. 'I hope you're comfortable,' she mocks.",
        "Mina grinds her feet into your skin, her smile never fading. 'You're tougher than you look,' she says."
    ], [
                  "Mina thinks you're a great mat.",
                  "Mina enjoys stepping on you.",
                  "Mina thinks you take a beating well.",
                  "Mina loves using you as her personal toy."
              ]),
    Character("Nejire", [
        "Nejire dehumanizes you and uses you as her seat, her smile sweet but her actions cruel. 'You're just a thing to me,' she says.",
        "Nejire mocks you while sitting on you, her weight pinning you down. 'You should be grateful,' she taunts.",
        "Nejire taunts you as she sits on your face, her laughter filled with malice. 'I could get used to this,' she admits.",
        "Nejire laughs at your helplessness, her feet pressing into you. 'You're nothing more than a cushion,' she says."
    ], [
                  "Nejire thinks you're a worthless thing.",
                  "Nejire enjoys using you as furniture.",
                  "Nejire loves your helplessness.",
                  "Nejire thinks you're beneath her."
              ]),
    Character("Tsuyu", [
        "Tsuyu kicks your balls, her expression unreadable. 'This is what you deserve,' she says flatly.",
        "Tsuyu stomps on your penis, her foot coming down hard. 'You're pathetic,' she mutters.",
        "Tsuyu laughs as she kicks you, her voice calm and collected. 'You like this, don't you?' she asks.",
        "Tsuyu grins while stomping on you, her eyes cold. 'Know your place,' she commands."
    ], [
                  "Tsuyu thinks you're pathetic.",
                  "Tsuyu enjoys seeing you in pain.",
                  "Tsuyu thinks you deserve every bit of it.",
                  "Tsuyu loves asserting her dominance."
              ]),
    Character("Nana", [
        "Nana gives you a footjob, her movements precise. 'Don't get too excited,' she warns.",
        "Nana laughs while stroking you with her feet, her touch both gentle and firm. 'You're enjoying this, aren't you?' she asks.",
        "Nana mocks you as you enjoy her footjob, her eyes glinting with amusement. 'You're so easy to please,' she teases.",
        "Nana teases you with her feet, her laughter ringing in your ears. 'Just a little more,' she says."
    ], [
                  "Nana thinks you're easy to please.",
                  "Nana enjoys teasing you.",
                  "Nana thinks you're beneath her.",
                  "Nana loves your reactions."
              ]),
    Character("Itsuka", [
        "Itsuka makes you behave like a dog, her commands sharp. 'Bark for me,' she orders.",
        "Itsuka forces you to bark like a dog, her laughter mocking. 'Good boy,' she says.",
        "Itsuka laughs as you crawl on all fours, her eyes filled with amusement. 'You're a natural,' she mocks.",
        "Itsuka taunts you with dog commands, her smile never fading. 'Roll over,' she commands."
    ], [
                  "Itsuka thinks you're pathetic.",
                  "Itsuka enjoys your humiliation.",
                  "Itsuka loves commanding you.",
                  "Itsuka thinks you're a good pet."
              ]),
    Character("Mt Lady", [
        "Mt Lady shrinks you and tapes you to her foot, her laughter booming. 'Enjoy the ride,' she says.",
        "Mt Lady laughs as you are stuck to her foot, her movements shaking you. 'Hold on tight,' she mocks.",
        "Mt Lady mocks your tiny size, her eyes gleaming with amusement. 'You're so small and pathetic,' she says.",
        "Mt Lady enjoys your helplessness, her foot dominating your world. 'You're mine now,' she declares."
    ], [
                  "Mt Lady thinks you're pathetic.",
                  "Mt Lady enjoys your helplessness.",
                  "Mt Lady thinks you're a good toy.",
                  "Mt Lady loves your tiny size."
              ]),
    Character("Toru", [
        "Toru finds you and crushes you under her foot, her laughter chilling. 'You can't escape,' she says.",
        "Toru laughs as you come back to life, her eyes filled with malice. 'You're fun to play with,' she mocks.",
        "Toru grinds her foot into you, her smile never fading. 'I love seeing you squirm,' she admits.",
        "Toru mocks you for being so weak, her laughter echoing. 'You're nothing to me,' she says."
    ], [
                  "Toru thinks you're weak.",
                  "Toru enjoys crushing you.",
                  "Toru thinks you're fun to play with.",
                  "Toru loves your suffering."
              ]),
    Character("Eri", [
        "Eri makes fun of you and makes you kiss her feet, her laughter innocent yet cruel. 'You're so pathetic,' she says.",
        "Eri laughs as you kiss her feet, her eyes gleaming. 'Do it again,' she orders.",
        "Eri mocks your pathetic state, her smile sweet. 'You're nothing,' she says.",
        "Eri enjoys degrading you, her laughter ringing in your ears. 'You're mine,' she declares."
    ], [
                  "Eri thinks you're pathetic.",
                  "Eri enjoys degrading you.",
                  "Eri thinks you're nothing.",
                  "Eri loves making you kiss her feet."
              ]),
    Character("Midnight", [
        "Midnight makes you eat bread from her toenails, her laughter sultry. 'Don't waste a crumb,' she teases.",
        "Midnight laughs as you eat from her feet, her eyes filled with amusement. 'Isn't it delicious?' she mocks.",
        "Midnight mocks your hunger, her voice dripping with sarcasm. 'You must be starving,' she says.",
        "Midnight enjoys your humiliation, her laughter echoing. 'You're such a good slave,' she taunts."
    ], [
                  "Midnight thinks you're a pathetic slave.",
                  "Midnight enjoys watching you eat from her feet.",
                  "Midnight thinks you're beneath her.",
                  "Midnight loves your humiliation."
              ]),
    Character("Mirko", [
        "Mirko makes you smell her shoes, her expression stern. 'Take a deep breath,' she orders.",
        "Mirko laughs as you sniff her shoes, her eyes cold. 'Do you like it?' she mocks.",
        "Mirko mocks your addiction to her scent, her voice filled with disdain. 'You're hopeless,' she says.",
        "Mirko enjoys your degradation, her laughter harsh. 'You're nothing but a foot slave,' she declares."
    ], [
                  "Mirko thinks you're hopeless.",
                  "Mirko enjoys your degradation.",
                  "Mirko thinks you're a perfect foot slave.",
                  "Mirko loves watching you suffer."
              ]),
    Character("Lady Nagant", [
        "Lady Nagant uses you as a footstool, her weight pressing down on you. 'Stay still,' she commands.",
        "Lady Nagant mocks you as she rests her feet on you, her smile cruel. 'You're good for something,' she says.",
        "Lady Nagant laughs at your helplessness, her eyes cold. 'You deserve this,' she taunts.",
        "Lady Nagant enjoys your suffering, her laughter echoing. 'You're beneath me,' she declares."
    ], [
                  "Lady Nagant thinks you're beneath her.",
                  "Lady Nagant enjoys your suffering.",
                  "Lady Nagant thinks you're a good footstool.",
                  "Lady Nagant loves asserting her dominance."
              ]),
    Character("Mei", [
        "Mei turns you into an insole and wears you for a day, her laughter ringing. 'Enjoy your new life,' she mocks.",
        "Mei laughs as you are stuck in her shoe, her movements shaking you. 'You're a perfect fit,' she says.",
        "Mei mocks your transformation, her voice filled with amusement. 'You're so much fun to play with,' she admits.",
        "Mei enjoys your discomfort, her laughter echoing. 'You belong to me now,' she declares."
    ], [
                  "Mei thinks you're a perfect insole.",
                  "Mei enjoys your discomfort.",
                  "Mei thinks you're fun to play with.",
                  "Mei loves having you under her feet."
              ]),
    Character("Inko", [
        "Inko wears you as an insole and throws you away, her laughter cold. 'You're nothing to me,' she says.",
        "Inko laughs as she steps on you, her weight pressing down. 'You belong in the trash,' she mocks.",
        "Inko mocks your existence, her voice filled with disdain. 'You're a pathetic slave,' she says.",
        "Inko enjoys your suffering, her laughter echoing. 'You're beneath me,' she declares."
    ], [
                  "Inko thinks you're trash.",
                  "Inko enjoys stepping on you.",
                  "Inko thinks you're a pathetic slave.",
                  "Inko loves your suffering."
              ])
]

# Define locations and their respective character appearances
locations = {
    "1. School": ["Kyoka", "Momo", "Ochako", "Tsuyu", "Itsuka"],
    "2. Cafe": ["Nejire", "Eri", "Lady Nagant"],
    "3. Grocery Store": ["Midnight", "Nana", "Mt Lady"],
    "4. Bank": ["Mina", "Mirko"],
    "5. Hospital": ["Himiko", "Toru", "Mei"]
}

player_responses = [
    "You feel disgusted by the smell of her feet, but you comply.",
    "You reluctantly follow her orders, feeling humiliated.",
    "You gag from the stench, but continue as commanded.",
    "You can't help but feel aroused despite the humiliation."
]


def encounter_girl(location, encountered):
    possible_girls = [char for char in characters if char.name in locations[location]]
    unencountered_girls = [girl for girl in possible_girls if girl.name not in encountered]

    if unencountered_girls:
        weights = [3 if girl.name in unencountered_girls else 1 for girl in possible_girls]
        girl = random.choices(possible_girls, weights=weights)[0]
    else:
        girl = random.choice(possible_girls)

    if girl.name not in encountered:
        encountered.add(girl.name)
    interaction = girl.interact()
    return girl, interaction


def check_remaining(encountered):
    all_girls = {char.name for char in characters}
    remaining = all_girls - encountered
    return remaining


def add_epilogue(choice, max_encounters):
    if choice == '1':
        if max_encounters.name == "Kyoka":
            print("""Upon making your choice, you find yourself at the mercy of Kyoka Jiro, embracing your role as her permanent foot slave. Kyoka looks down at you with a smirk, her eyes filled with a mix of amusement and superiority. "I knew you'd make the right choice," she says, her voice dripping with confidence. The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.

            Every morning starts with you waking up on a small mat at the foot of Kyoka's bed. She stretches with a languid yawn, her feet just inches from your face. "Morning, slave," she says, wiggling her toes in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Kyoka’s mornings are filled with a casual authority that keeps you in your place.
            
            Your duties revolve around pampering Kyoka's feet and enduring her various whims. She loves making you lick her feet clean after her workouts, enjoying the taste of your humiliation. "Get every spot," she commands with a smirk, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Throughout the day, Kyoka incorporates you into her various activities, always finding new ways to torment and amuse herself. She takes pleasure in pushing your limits, using you as her personal footrest and face seat. "Hold still," she commands, pressing her feet into your face with playful cruelty. The pain is sharp, but you endure it, knowing it serves her amusement. "You're such a fun toy," she says, inspecting her work. "I can play with you all day."
            
            Kyoka’s friends visit frequently, and she takes great delight in showing off her obedient foot slave. Momo, Mina, and the others find endless amusement in your presence. "Jiro, your slave is quite resilient," Momo remarks as she steps on you. Kyoka beams with pride, enjoying the attention. "Yeah, he knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of playful chaos and degradation. Kyoka lounges on the couch, her feet resting on your face as she watches TV or plays her guitar. She loves rock music, and the scenes in her room often mirror the intensity of your situation. "Isn't this the best?" she asks, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her music while using you as her personal ottoman.
            
            One day, Kyoka decides to take you to her favorite cafe, leading you on a leash like a pet. The humiliation of being paraded around in public is overwhelming. "This will be fun," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you carry her bags and fetch her drinks, ensuring that everyone in the cafe notices your predicament. "You’re so lucky to serve me," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Kyoka’s cafe trips become both your torture and your routine. She has a special spot reserved for you, where you kneel beside her, ready to serve her at a moment's notice. "This is where you belong," she says, pointing to the floor. You stay there every time she visits the cafe, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Kyoka ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Kyoka Jiro’s foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Kyoka’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a casual, almost nonchalant, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a smirk, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Kyoka occasionally opens up about her life, sharing stories of her musical ambitions and dreams. "Being a hero and a musician is a lot of work," she admits one evening, her feet resting on your chest. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            Kyoka’s cafe trips often involve you in her playful antics. She enjoys making you fetch items for her, sometimes tying you up with ropes to test your agility and obedience. "Hold still, slave," she commands, binding you tightly. The ropes dig into your skin, but you endure it, knowing that you are serving her. "Perfect," she says, inspecting her work. "You are quite useful."
            
            Your life as Kyoka Jiro’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. But over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Kyoka Jiro is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Kyoka. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her playful face, knowing that you exist solely for her pleasure.
            
            Kyoka’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Kyoka’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her chair while she practices her guitar. She binds you in a crouched position, her weight pressing down on you as she calmly strums her instrument. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Kyoka's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Kyoka shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Kyoka. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")
        elif max_encounters.name == "Ochako":
            print("""After making your choice, you find yourself at the mercy of Ochako Uraraka, embracing your role as her permanent foot slave. Ochako looks down at you with a mix of curiosity and amusement, her eyes twinkling with excitement. "I never thought I'd have my own foot slave," she says with a giggle, flexing her toes. The sweet yet pungent scent of her feet fills your nostrils, solidifying your new reality.
            
            Every morning starts with you waking up on a small mat at the foot of Ochako's bed. She stretches gracefully, her feet just inches from your face. "Good morning, slave," she says cheerfully, wiggling her toes in front of you. You respond with a respectful kiss on each toe, knowing that your day begins and ends with her command. Ochako’s mornings are filled with laughter and light-heartedness, but you know better than to underestimate her.
            
            Your duties revolve around pampering Ochako's feet and enduring her various whims. She loves making you lick her feet clean after her workouts, enjoying the taste of your humiliation. "Get every spot," she instructs with a smile, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Throughout the day, Ochako integrates you into her routine in various ways. When she practices her Quirk or trains, you are there to massage her feet during breaks. She loves how your hands feel against her tired soles. "You're pretty good at this," she says with a grin, and you take pride in your work, despite the demeaning nature of your tasks.
            
            Ochako’s friends visit often, and she delights in showing off her obedient foot slave. Tsuyu, Momo, and the others find endless amusement in your presence. "Uraraka, your slave is quite handy," Tsuyu remarks as she uses you as a footrest. Ochako beams with pride, enjoying the attention. "Yeah, he's really useful," she replies, her voice tinged with pride.
            
            Evenings are a mix of relaxation and degradation. Ochako lounges on the couch, her feet resting on your face as she watches TV. She loves romantic comedies, and the laughter on the screen contrasts sharply with the reality of your situation. "Isn't this fun?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response would lead to punishment. "Good," she says, focusing back on the TV while using you as her personal ottoman.
            
            One night, Ochako decides to take you out for a walk, leading you on a leash like a pet. The streets are quiet, but the humiliation of being paraded around is overwhelming. "Isn't this nice?" she asks, her voice cheerful. You nod, knowing that any answer other than agreement will result in punishment. She leads you to a quiet park, where she makes you massage her feet under the stars. "You're so lucky to serve me," she says, her voice soft but commanding. You nod again, fully aware of your place.
            
            Ochako’s bedroom is both your sanctuary and your prison. She has a small mat and a pillow for you in the corner. "This is where you belong," she says, pointing to the corner. You sleep there every night, curled up at her feet, ready to serve her at a moment's notice. The nights are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Ochako ensures that you eat just enough to stay functional. "We don't want you getting lazy," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Ochako Uraraka's foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Ochako’s cruelty is masked by her cheerful demeanor. She takes pleasure in pushing your limits with a sweet smile. One day, she decides to test your loyalty by making you lick her feet clean after a long day. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a giggle, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Ochako occasionally opens up about her life, sharing stories of her struggles and dreams. "Being a hero is tough," she admits one evening, her feet resting on your chest. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            Ochako’s favorite pastime is having you rub her feet after a long day. She often makes you kneel in front of her as she relaxes, placing her sweaty, tired feet in your hands. "Make sure you get all the sore spots," she instructs, her voice firm yet playful. You comply, feeling the roughness of her soles and the smell of her sweat, knowing that your discomfort brings her pleasure. "You have no idea how much I needed this," she sighs contentedly, leaning back and closing her eyes.
            
            Your life as Ochako Uraraka's foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. But over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Ochako Uraraka is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Ochako. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her smiling face, knowing that you exist solely for her pleasure.
            
            Ochako’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You're doing great," she says, patting your head as you work.
            
            Ochako’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You're doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Ochako's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Ochako shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Ochako. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Momo":
            print("""Upon making your choice, you find yourself bound to Momo Yaoyorozu, embracing your role as her permanent foot slave. Momo looks down at you with a composed yet commanding gaze, her eyes filled with a mix of authority and curiosity. "I have high expectations for you," she declares, her tone firm yet calm. The scent of her feet envelops you, marking the beginning of your new life.
            
            Every morning begins with you waking up on a small mat at the foot of Momo's bed. She stretches elegantly, her feet just inches away from your face. "Good morning, slave," she says softly but firmly. You respond by kissing each toe with reverence, knowing that your day starts and ends with her command. Momo's mornings are filled with rigorous schedules and disciplined routines, and you quickly learn to adapt.
            
            Your duties extend beyond merely pampering Momo's feet. She is a woman of intellect and sophistication, and she finds ways to involve you in her various projects. Whether it's helping her organize her study materials or assisting with her training sessions, you are always by her side, ready to serve. "Make sure everything is perfect," she instructs, her tone leaving no room for error. You comply diligently, knowing that her satisfaction is paramount.
            
            Throughout the day, Momo incorporates you into her intense training and study sessions. She practices her combat techniques with you as her dummy, binding you with ropes she creates, testing their strength and flexibility. "Hold still," she commands, securing you tightly. The ropes dig into your skin, but you endure the discomfort, knowing it serves her purpose. "Excellent," she says, inspecting her work. "You are quite useful."
            
            Momo’s friends visit frequently, and she takes great pride in demonstrating your obedience. Jiro, Mina, and the others find endless amusement in your presence. "Yaoyorozu, your slave is quite diligent," Jiro remarks as she uses you as a footstool. Momo smiles with pride, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with superiority.
            
            Evenings are a mix of intellectual pursuits and physical degradation. Momo often has you read to her while she rests her feet on your back or face. She loves classical literature and philosophical texts, and you read aloud, your voice trembling slightly under the weight of her feet. "Isn't this enlightening?" she asks, her toes tapping your nose lightly. You nod, understanding that any response other than agreement could lead to punishment. "Good," she says, continuing to enjoy her book while using you as her personal furniture.
            
            One night, Momo decides to take you to her private laboratory. She leads you on a leash, the humiliation of being paraded around almost unbearable. "This will be an educational experience for you," she says, her tone firm yet kind. You nod, knowing that any response other than compliance would be unacceptable. She makes you assist in her experiments, often using you to test the practicality of her creations. "You’re so fortunate to serve me," she says, her voice soft but commanding. You nod again, fully aware of your place.
            
            Momo’s laboratory becomes both your sanctuary and your prison. She has a small corner set up for you, complete with a mat and a pillow. "This is where you belong," she says, pointing to the corner. You sleep there every night, ready to serve her at a moment's notice. The nights are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Momo ensures that you eat just enough to stay functional. "We don't want you getting lazy," she says with a gentle yet firm tone, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Momo Yaoyorozu's foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Momo’s cruelty is masked by her composed demeanor. She takes pleasure in pushing your limits with a calm, almost nurturing, approach. One day, she decides to test your loyalty by making you lick her feet clean after a long day. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a soft smile, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Momo occasionally opens up about her life, sharing stories of her responsibilities and aspirations. "Being a hero and a leader is demanding," she admits one evening, her feet resting on your chest. "But having you here makes it a bit more manageable." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            Momo’s intellectual pursuits often involve you in her experiments. She enjoys using you to test her creations, sometimes tying you up with ropes she generates, testing their strength and flexibility. "Hold still, slave," she commands, binding you tightly. The ropes dig into your skin, but you endure it, knowing that you are serving her. "Perfect," she says, inspecting her work. "You are quite useful."
            
            One of Momo's favorite ways to test your loyalty is by making you lick her dirty, smelly soles. After a long day, she takes off her shoes and places her feet in front of you. "Clean them thoroughly," she orders, her eyes watching you closely. The smell is overwhelming, but you lean in and start licking, the taste of sweat and grime filling your mouth. "Good, make sure you get every inch," she says, leaning back and enjoying the sensation. Your tongue moves across her soles, cleaning them as best as you can. "You’re doing well," she says, her voice filled with satisfaction. "Keep going."
            
            Your life as Momo Yaoyorozu's foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. But over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Momo Yaoyorozu is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Momo. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her composed face, knowing that you exist solely for her pleasure.
            
            Momo’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a calm smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire estate, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You're doing well," she says, patting your head as you work.
            
            Momo’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her chair while she practices her martial arts forms. She binds you in a crouched position, her weight pressing down on you as she calmly moves through her routine. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Momo's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Momo shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Momo. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Your daily routine with Momo includes more than just tending to her feet. She involves you in her academic pursuits, making you fetch her books and materials, and even assisting her in experiments. "You need to be useful in all aspects," she says, her tone firm yet nurturing. You strive to meet her high expectations, knowing that your performance is a direct reflection of your worth to her.
            
            Momo's friends, always intrigued by your presence, continue to visit. They take turns using you as their footstool or testing your endurance in various humiliating tasks. Each visit reinforces your place in this world, and Momo watches with a satisfied smile. "He's here to serve," she tells them, her voice filled with pride.
            
            One evening, Momo decides to challenge you further. "I want to see how well you handle prolonged tasks," she says, her eyes glinting with curiosity. She ties you up and makes you balance a book on your head while licking her feet. The task is grueling, but you push through, driven by the desire to please her. "Good job," she says softly when you finally complete it, her words a rare moment of praise.
            
            Despite the constant demands and humiliations, you find moments of twisted solace in your servitude. Each task, no matter how degrading, is a chance to prove your loyalty and dedication to Momo. You cling to these moments, finding a strange comfort in your role.
            
            Momo's intellectual pursuits often lead to experiments where you are the subject. She tests various formulas and gadgets on you, always with a clinical detachment. "Hold still," she commands, adjusting a device strapped to your body. The sensations range from discomfort to intense pain, but you endure it all, knowing it's for her benefit. "Interesting," she muses, taking notes. "You are quite resilient."
            
            In her private moments, Momo occasionally shares glimpses of vulnerability. "Being a hero and a leader is a heavy burden," she confides one night, her feet resting on your chest. "But having you here makes it a bit more manageable." These moments of connection, though rare, give you a sense of purpose beyond your servitude. You are her confidant, her silent support.
            
            As the months turn into years, your identity as Momo's foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Momo. You exist solely for her pleasure and comfort.
            
            Momo's cruelty, though ever-present, is tempered by her meticulous care. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Momo. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Momo's demands continue to evolve, always pushing you to your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Momo. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Momo Yaoyorozu is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Himiko":
            print("""After making your choice, you find yourself at the mercy of Himiko Toga, embracing your role as her permanent foot slave. Himiko looks down at you with a mischievous glint in her eyes, her smile wide and sinister. "I’m going to have so much fun with you," she says, her voice dripping with excitement. The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Himiko's bed. She stretches with a playful yawn, her feet just inches from your face. "Morning, slave," she says cheerfully, wiggling her toes in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Himiko’s mornings are filled with chaotic energy, setting the tone for your unpredictable life.
            
            Your duties revolve around pampering Himiko's feet and enduring her various whims. She loves making you lick her feet clean after her workouts, enjoying the taste of your humiliation. "Get every spot," she commands with a giggle, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Throughout the day, Himiko incorporates you into her various activities, always finding new ways to torment and amuse herself. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her. "Hold still," she commands, pressing her feet into your face with playful cruelty. The pain is sharp, but you endure it, knowing it serves her amusement. "You're such a fun toy," she says, inspecting her work. "I can play with you all day."
            
            Himiko’s friends from the League of Villains visit frequently, and she takes great delight in showing off her obedient foot slave. Twice, Dabi, and the others find endless amusement in your presence. "Toga, your slave is quite durable," Dabi remarks as he steps on you. Himiko beams with pride, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with excitement.
            
            Evenings are a mix of chaos and degradation. Himiko lounges on the couch, her feet resting on your face as she watches TV or plans her next heist. She loves crime dramas, and the scenes on the screen often reflect the reality of your situation. "Isn't this thrilling?" she asks, her toes pressing against your nose. You nod, knowing that any other response would lead to punishment. "Good," she says, focusing back on the TV while using you as her personal ottoman.
            
            One night, Himiko decides to take you to the gym, leading you on a leash like a pet. The humiliation of being paraded around is overwhelming. "This will be fun," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you perform various exercises, using you as her personal trainer and equipment. "You’re so lucky to serve me," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Himiko’s gym sessions become both your torture and your routine. She has a small corner set up for you, complete with a mat and a water bottle. "This is where you belong," she says, pointing to the corner. You stay there every night, ready to serve her at a moment's notice. The nights are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Himiko ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Himiko Toga’s foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Himiko’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a chaotic, almost childlike, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a wide grin, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Himiko occasionally opens up about her life, sharing stories of her chaotic upbringing and twisted desires. "Being a villain is so much fun," she admits one evening, her feet resting on your chest. "And having you here makes it even better." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            Himiko’s gym sessions often involve you in her workouts. She enjoys using you as her bench press, sometimes tying you up with ropes to test your strength and endurance. "Hold still, slave," she commands, binding you tightly. The ropes dig into your skin, but you endure it, knowing that you are serving her. "Perfect," she says, inspecting her work. "You are quite useful."
            
            One of Himiko's favorite methods of domination involves deepthroating you with her feet. After a particularly intense workout, she makes you lie on your back, placing her sweaty feet over your mouth. "Open wide," she commands, her voice filled with excitement. You comply, opening your mouth as wide as you can. She begins to force her toes deep into your throat, enjoying the way you gag and struggle. "Doesn't this feel amazing?" she asks, her eyes glinting with sadistic pleasure. You choke and gag, the taste and smell overwhelming, but you endure it for her approval. "Good job," she says, patting your head. "You took that so well."
            
            Your life as Himiko Toga’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. But over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Himiko Toga is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Himiko. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her mischievous face, knowing that you exist solely for her pleasure.
            
            Himiko’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Himiko’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her chair while she practices her knife skills. She binds you in a crouched position, her weight pressing down on you as she calmly sharpens her blades. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her work.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Himiko's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Himiko shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused onserving Himiko. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Himiko’s demands continue to evolve, always pushing you to your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Himiko. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Himiko Toga is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Your daily routine with Himiko includes more than just tending to her feet. She involves you in her chaotic lifestyle, making you fetch her tools and materials, and even assisting her in planning her next heist. "You need to be useful in all aspects," she says, her tone firm yet nurturing. You strive to meet her high expectations, knowing that your performance is a direct reflection of your worth to her.
            
            Himiko's friends, always intrigued by your presence, continue to visit. They take turns using you as their footstool or testing your endurance in various humiliating tasks. Each visit reinforces your place in this world, and Himiko watches with a satisfied smile. "He's here to serve," she tells them, her voice filled with pride.
            
            One evening, Himiko decides to challenge you further. "I want to see how well you handle prolonged tasks," she says, her eyes glinting with curiosity. She ties you up and makes you balance a book on your head while licking her feet. The task is grueling, but you push through, driven by the desire to please her. "Good job," she says softly when you finally complete it, her words a rare moment of praise.
            
            Despite the constant demands and humiliations, you find moments of twisted solace in your servitude. Each task, no matter how degrading, is a chance to prove your loyalty and dedication to Himiko. You cling to these moments, finding a strange comfort in your role.
            
            Himiko's intellectual pursuits often lead to experiments where you are the subject. She tests various formulas and gadgets on you, always with a clinical detachment. "Hold still," she commands, adjusting a device strapped to your body. The sensations range from discomfort to intense pain, but you endure it all, knowing it's for her benefit. "Interesting," she muses, taking notes. "You are quite resilient."
            
            In her private moments, Himiko occasionally shares glimpses of vulnerability. "Being a villain is exhilarating," she confides one night, her feet resting on your chest. "And having you here makes it even better." These moments of connection, though rare, give you a sense of purpose beyond your servitude. You are her confidant, her silent support.
            
            As the months turn into years, your identity as Himiko's foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Himiko. You exist solely for her pleasure and comfort.
            
            Himiko's cruelty, though ever-present, is tempered by her meticulous care. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Himiko. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Himiko’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Himiko. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Himiko Toga is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Mina":
            print("""After making your choice, you find yourself at the mercy of Mina Ashido, embracing your role as her permanent foot slave. Mina looks down at you with a gleeful sparkle in her eyes, her smile wide and mischievous. "We're going to have so much fun," she says, her voice dripping with excitement. The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Mina's bed. She stretches energetically, her feet just inches from your face. "Morning, slave," she says cheerfully, wiggling her toes in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Mina’s mornings are filled with spontaneous bursts of energy, setting the tone for your unpredictable life.
            
            Your duties revolve around pampering Mina's feet and enduring her playful yet cruel whims. She loves making you lick her feet clean after her workouts, enjoying the taste of your humiliation. "Get every spot," she commands with a giggle, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Throughout the day, Mina incorporates you into her various activities, always finding new ways to torment and amuse herself. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her. "Hold still," she commands, pressing her feet into your face with playful cruelty. The pain is sharp, but you endure it, knowing it serves her amusement. "You're such a fun toy," she says, inspecting her work. "I can play with you all day."
            
            Mina’s friends visit frequently, and she takes great delight in showing off her obedient foot slave. Kirishima, Sero, and the others find endless amusement in your presence. "Ashido, your slave is quite durable," Kirishima remarks as he steps on you. Mina beams with pride, enjoying the attention. "Yeah, he's pretty tough," she replies, her voice tinged with pride.
            
            Evenings are a mix of playful chaos and degradation. Mina lounges on the couch, her feet resting on your face as she watches TV or plays video games. She loves action comedies, and the scenes on the screen often mirror the intensity of your situation. "Isn't this hilarious?" she asks, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One day, Mina decides to take you grocery shopping, leading you on a leash like a pet. The humiliation of being paraded around in public is overwhelming. "This will be fun," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you carry the shopping bags, ensuring that everyone in the store notices your predicament. "You’re so lucky to serve me," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Mina’s grocery trips become both your torture and your routine. She has a special corner in her kitchen set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the corner. You stay there every evening, ready to serve her at a moment's notice. The nights are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Mina ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Mina Ashido’s foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Mina’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a cheerful, almost childlike, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a wide grin, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Mina occasionally opens up about her life, sharing stories of her chaotic adventures and dreams. "Being a hero is so exciting," she admits one evening, her feet resting on your chest. "And having you here makes it even more fun." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One of Mina's favorite methods of domination is trampling you. After a long day, she makes you lie on the floor and steps on you, her weight pressing down on your chest and face. "Doesn't this feel great?" she asks with a giggle, her feet digging into your skin. You groan in pain, but you endure it for her amusement. "I love how squishy you are," she says, her eyes filled with delight. "You're the perfect foot mat."
            
            Mina’s grocery trips often involve you in her playful antics. She enjoys making you fetch items for her, sometimes tying you up with ropes to test your agility and obedience. "Hold still, slave," she commands, binding you tightly. The ropes dig into your skin, but you endure it, knowing that you are serving her. "Perfect," she says, inspecting her work. "You are quite useful."
            
            Your life as Mina Ashido’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. But over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Mina Ashido is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Mina. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her playful face, knowing that you exist solely for her pleasure.
            
            Mina’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Mina’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her chair while she paints her nails. She binds you in a crouched position, her weight pressing down on you as she calmly applies the polish. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her work.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Mina's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Mina shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Mina. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Nejire":
            print("""After making your choice, you find yourself at the mercy of Nejire Hado, embracing your role as her permanent foot slave. Nejire looks down at you with a curious and excited expression, her smile wide and radiant. "This is going to be so much fun!" she exclaims, her voice filled with joy. The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Nejire's bed. She stretches with a graceful yawn, her feet just inches from your face. "Good morning, slave," she says cheerfully, wiggling her toes in front of you. You respond with a respectful kiss on each toe, knowing that your day begins and ends with her command. Nejire’s mornings are filled with vibrant energy that keeps you on your toes, literally and figuratively.
            
            Your duties revolve around pampering Nejire's feet and enduring her playful yet demanding whims. She loves making you lick her feet clean after her daily activities, relishing the taste of your humiliation. "Make sure you get every spot," she commands with a giggle, her eyes sparkling with amusement. You comply diligently, aware that her satisfaction is your only reward.
            
            Throughout the day, Nejire incorporates you into her various activities, always finding new ways to torment and amuse herself. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her. "Hold still," she commands, pressing her feet into your face with playful cruelty. The pain is sharp, but you endure it, knowing it serves her amusement. "You're such a fun toy," she says, inspecting her work. "I can play with you all day."
            
            Nejire’s friends visit frequently, and she takes great delight in showing off her obedient foot slave. Mirio, Tamaki, and the others find endless amusement in your presence. "Hado, your slave is quite resilient," Mirio remarks as he steps on you. Nejire beams with pride, enjoying the attention. "Yeah, he's pretty tough," she replies, her voice tinged with pride.
            
            Evenings are a mix of playful chaos and degradation. Nejire lounges on the couch, her feet resting on your face as she watches TV or chats with her friends. She loves romantic comedies, and the laughter on the screen contrasts sharply with the reality of your situation. "Isn't this fun?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response would lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One day, Nejire decides to take you to her favorite café, leading you on a leash like a pet. The humiliation of being paraded around in public is overwhelming. "This will be fun," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you carry her bags and fetch her drinks, ensuring that everyone in the café notices your predicament. "You’re so lucky to serve me," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Nejire’s café trips become both your torture and your routine. She has a special spot reserved for you, where you kneel beside her, ready to serve her at a moment's notice. "This is where you belong," she says, pointing to the floor. You stay there every time she visits the café, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Nejire ensures that you eat just enough to stay functional. "We don't want you getting lazy," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Nejire Hado's foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Nejire’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a cheerful, almost childlike, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a wide grin, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Nejire occasionally opens up about her life, sharing stories of her adventures and dreams. "Being a hero is so exciting," she admits one evening, her feet resting on your chest. "And having you here makes it even more fun." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One of Nejire's favorite methods of domination is sitting on your face. After a long day, she makes you lie down and straddles your head, her weight pressing down on you. "This is so comfy," she says with a playful smile, her feet resting on your face as well. The scent and pressure are overwhelming, but you endure it for her pleasure. "You're the perfect cushion," she says, her eyes filled with delight.
            
            Nejire’s café trips often involve you in her playful antics. She enjoys making you fetch items for her, sometimes tying you up with ropes to test your agility and obedience. "Hold still, slave," she commands, binding you tightly. The ropes dig into your skin, but you endure it, knowing that you are serving her. "Perfect," she says, inspecting her work. "You are quite useful."
            
            Your life as Nejire Hado’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. But over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Nejire Hado is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Nejire. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her playful face, knowing that you exist solely for her pleasure.
            
            Nejire’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Nejire’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Nejire's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Nejire shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Nejire. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Nejire. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Nejire’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Nejire. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Nejire’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Nejire. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Nejire Hado is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Each day starts with you waking up at Nejire's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Nejire shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Nejire. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Nejire’s demands continue to evolve, always pushing you to your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Nejire. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Nejire Hado is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Tsuyu":
            print("""After making your choice, you find yourself at the mercy of Tsuyu Asui, embracing your role as her permanent foot slave. Tsuyu looks down at you with a cold, calculating gaze, her eyes devoid of mercy. "This will be interesting," she says with a hint of amusement in her voice. The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Tsuyu's bed. She stretches with a languid yawn, her feet just inches from your face. "Morning, slave," she says flatly, her expression unreadable. You respond with a respectful kiss on each toe, knowing that your day begins and ends with her command. Tsuyu’s mornings are filled with a quiet intensity that keeps you on edge, never knowing what to expect.
            
            Your duties revolve around pampering Tsuyu's feet and enduring her various whims. She loves making you lick her feet clean after her training sessions, relishing the taste of your humiliation. "Get every spot," she instructs with a stern voice, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Throughout the day, Tsuyu incorporates you into her various activities, always finding new ways to torment and amuse herself. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her. "Hold still," she commands, pressing her feet into your face with a mixture of cruelty and detachment. The pain is sharp, but you endure it, knowing it serves her amusement. "You're pathetic," she says, inspecting her work. "But you're useful."
            
            Tsuyu’s friends visit frequently, and she takes great delight in showing off her obedient foot slave. Ochako, Momo, and the others find endless amusement in your presence. "Asui, your slave is quite durable," Momo remarks as she steps on you. Tsuyu nods with a smirk, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of sadistic play and degradation. Tsuyu lounges on the couch, her feet resting on your face as she watches TV. She loves nature documentaries, and the serene scenes on the screen contrast sharply with the reality of your situation. "Isn't this fascinating?" she asks, her toes pressing against your nose. You nod, knowing that any other response would lead to punishment. "Good," she says, focusing back on the TV while using you as her personal ottoman.
            
            One day, Tsuyu decides to take you to her favorite training spot, leading you on a leash like a pet. The humiliation of being paraded around in public is overwhelming. "This will be fun," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you carry her gear and fetch her drinks, ensuring that everyone in the area notices your predicament. "You’re so lucky to serve me," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Tsuyu’s training sessions become both your torture and your routine. She has a special corner set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the corner. You stay there every evening, ready to serve her at a moment's notice. The nights are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Tsuyu ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Tsuyu Asui’s foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Tsuyu’s cruelty is masked by her calm demeanor. She takes pleasure in pushing your limits with a cold, almost clinical, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a smirk, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Tsuyu occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your chest. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One of Tsuyu's favorite methods of domination is ballbusting. After a particularly grueling training session, she makes you lie on your back, spreading your legs wide. "This is going to hurt," she says with a cold smile, lifting her foot and slamming it down onto your groin. The pain is excruciating, but you endure it for her amusement. "You're so pathetic," she says, her eyes filled with contempt. "But you're mine."
            
            Tsuyu’s training sessions often involve you in her playful yet sadistic antics. She enjoys making you fetch items for her, sometimes tying you up with ropes to test your agility and obedience. "Hold still, slave," she commands, binding you tightly. The ropes dig into your skin, but you endure it, knowing that you are serving her. "Perfect," she says, inspecting her work. "You are quite useful."
            
            Tsuyu's friends are frequently invited to join in the fun. One evening, she calls them over for a special session. "Watch this," she says, her voice filled with excitement. She makes you lick her feet in front of them, the humiliation intensified by their presence. "Isn't he pathetic?" she asks, her friends nodding in agreement. Then, she delivers a sharp kick to your balls, the pain doubling as the girls laugh. "You're a perfect plaything," Tsuyu says, her voice dripping with satisfaction.
            
            Despite the constant degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Tsuyu. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Tsuyu’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Tsuyu. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Tsuyu Asui is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Each day starts with you waking up at Tsuyu's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Tsuyu shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Tsuyu. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Nana":
            print("""Upon making your choice, you find yourself at the mercy of Nana Shimura, embracing your role as her permanent foot slave. Nana looks down at you with a mixture of authority and amusement, her eyes glinting with dominance. "I hope you're ready for this," she says with a confident smile. The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Nana's bed. She stretches with a graceful yawn, her feet just inches from your face. "Morning, slave," she says warmly but firmly, wiggling her toes in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Nana’s mornings are filled with a serene yet commanding energy, setting the tone for your life of servitude.
            
            Your duties revolve around pampering Nana's feet and enduring her various whims. She loves making you lick her feet clean after her daily activities, enjoying the taste of your humiliation. "Make sure you get every spot," she instructs with a gentle yet authoritative tone, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Throughout the day, Nana incorporates you into her various routines, always finding new ways to utilize and amuse herself with your presence. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her. "Hold still," she commands, pressing her feet into your face with controlled dominance. The pain is sharp, but you endure it, knowing it serves her amusement. "You're doing well," she says, inspecting her work. "Keep it up."
            
            Nana’s friends and acquaintances visit frequently, and she takes great delight in showing off her obedient foot slave. All Might, Gran Torino, and the others find endless amusement in your presence. "Shimura, your slave is quite resilient," All Might remarks as he steps on you. Nana beams with pride, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of serene control and intense degradation. Nana lounges on the couch, her feet resting on your face as she watches TV or reads a book. She loves historical dramas, and the scenes on the screen often mirror the intensity of your situation. "Isn't this fascinating?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One day, Nana decides to take you to the park, leading you on a leash like a pet. The humiliation of being paraded around in public is overwhelming. "This will be good for you," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you carry her bags and fetch her refreshments, ensuring that everyone in the park notices your predicament. "You’re so lucky to serve me," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Nana’s park visits become both your torture and your routine. She has a special spot set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the spot. You stay there every time she visits the park, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Nana ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Nana Shimura’s foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Nana’s cruelty is masked by her calm demeanor. She takes pleasure in pushing your limits with a composed, almost nurturing, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a soft smile, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Nana occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your chest. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One of Nana's favorite methods of domination is giving you footjobs. After a long day, she makes you lie down and straddles your body, her feet skillfully pleasuring you. "You’re my personal masturbating device," she says with a smirk, her feet moving with practiced ease. The sensation is overwhelming, but you endure it, knowing it serves her desires. "You like this, don’t you?" she asks, her eyes filled with satisfaction. You nod, unable to speak, fully immersed in your role. "Good," she says, her voice a mixture of dominance and amusement.
            
            During one of her park visits, Nana decides to involve the public in your humiliation. She leads you on a leash, making you crawl behind her. "Let’s see how well you perform under public scrutiny," she says with a wicked smile. She stops by a group of women sitting on a bench and introduces you. "This is my foot slave," she announces, her voice filled with pride. The women laugh and take turns using you, making you lick their dirty feet and grovel at their command. "He’s quite obedient," one of them remarks, kicking your balls for added humiliation. "Yes, he’s well-trained," Nana replies, watching with satisfaction.
            
            Your life as Nana Shimura’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. But over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Nana Shimura is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Nana. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her serene face, knowing that you exist solely for her pleasure.
            
            Nana’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Nana’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her chair while she practices her combat skills. She binds you in a crouched position, her weight pressing down on you as she calmly focuses on her moves. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Nana's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Nana shows a softer side, acknowledging your efforts in her own twisted way. You cherish these moments, even though they are fleeting and always come with a price.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Nana. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Nana’s demands continue to evolve, always pushing you to your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Nana. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Nana Shimura is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Each day starts with you waking up at Nana's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Nana shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Nana. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Nana’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Nana. You exist solely for her pleasure and comfort.
            
            Nana’s cruelty, though ever-present, is tempered by her nurturing nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Nana. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Nana’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Nana. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Nana Shimura is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Nana's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Nana shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Nana. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Nana’s demands continue to evolve, always pushing you to your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Nana. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Nana Shimura is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Itsuka":
            print("""Upon making your choice, you find yourself at the mercy of Itsuka Kendo, embracing your role as her permanent foot slave. Itsuka looks down at you with a mixture of authority and amusement, her eyes glinting with a hint of cruelty. "From now on, you’re not a person, you’re just my pet," she declares with a confident smile. "I’m going to call you Spot." The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Itsuka's bed. She stretches with a graceful yawn, her feet just inches from your face. "Morning, Spot," she says warmly but firmly, wiggling her toes in front of you. You respond by licking each toe with reverence, knowing that your day begins and ends with her command. Itsuka’s mornings are filled with a commanding energy, setting the tone for your life of servitude.
            
            Your duties revolve around pampering Itsuka's feet and enduring her various whims. She loves making you lick her feet clean after her training sessions, relishing the taste of your humiliation. "Get every spot, Spot," she instructs with a gentle yet authoritative tone, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Throughout the day, Itsuka incorporates you into her various routines, always finding new ways to utilize and amuse herself with your presence. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her on all fours. "Hold still, Spot," she commands, pressing her feet into your face with controlled dominance. The pain is sharp, but you endure it, knowing it serves her amusement. "Good boy," she says, inspecting her work. "You’re such a good pet."
            
            Itsuka’s friends and acquaintances visit frequently, and she takes great delight in showing off her obedient pet. Momo, Kyoka, and the others find endless amusement in your presence. "Kendo, your pet is quite resilient," Momo remarks as she steps on you. Itsuka beams with pride, enjoying the attention. "Yes, Spot knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of serene control and intense degradation. Itsuka lounges on the couch, her feet resting on your face as she watches TV or reads a book. She loves action dramas, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, Spot?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good boy," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One day, Itsuka decides to take you to the park, leading you on a leash like a dog. The humiliation of being paraded around in public is overwhelming. "This will be good for you," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you carry her bags and fetch her refreshments, ensuring that everyone in the park notices your predicament. "You’re so lucky to serve me, Spot," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Itsuka’s park visits become both your torture and your routine. She has a special spot set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the spot. You stay there every time she visits the park, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Itsuka ensures that you eat just enough to stay functional. "We don’t want you getting lazy, Spot," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Itsuka Kendo’s pet, Spot. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Itsuka’s cruelty is masked by her calm demeanor. She takes pleasure in pushing your limits with a composed, almost nurturing, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this, Spot," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good boy," she says with a soft smile, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Itsuka occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your chest. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One of Itsuka's favorite methods of domination is making you lick the sweat off her feet like a dog. After a particularly grueling training session, she makes you lie on the floor and puts her sweaty feet in your face. "Lick them clean, Spot," she commands, her voice filled with authority. The taste is overwhelming, but you endure it, knowing it serves her desires. "Good boy," she says, her eyes filled with satisfaction. "You’re such a good pet."
            
            During one of her park visits, Itsuka decides to involve the public in your humiliation. She leads you on a leash, making you crawl behind her. "Let’s see how well you perform under public scrutiny," she says with a wicked smile. She stops by a group of women sitting on a bench and introduces you. "This is my pet, Spot," she announces, her voice filled with pride. The women laugh and take turns using you, making you lick their dirty feet and grovel at their command. "He’s quite obedient," one of them remarks, kicking you for added humiliation. "Yes, Spot is well-trained," Itsuka replies, watching with satisfaction.
            
            Your life as Itsuka Kendo’s pet is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. But over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her pet, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Itsuka Kendo is your mistress, and you are her obedient, devoted pet, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Itsuka. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her serene face, knowing that you exist solely for her pleasure.
            
            Itsuka’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are, Spot," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "Good boy," she says, patting your head as you work.
            
            Itsuka’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her chair while she practices her martial arts. She binds you in a crouched position, her weight pressing down on you as she calmly moves through her forms. "Stay still, Spot," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "Good boy," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their pet, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Itsuka's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Itsuka shows a softer side, acknowledging your efforts in her own twisted way. You cherish these moments, even though they are fleeting and always come with a price.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her pet. Each day blends into the next, with your entire being focused on serving Itsuka. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Itsuka’s pet solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Itsuka. You exist solely for her pleasure and comfort.
            
            Itsuka’s cruelty, though ever-present, is tempered by her nurturing nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best, Spot," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Itsuka. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Itsuka’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me, Spot," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Itsuka. You have accepted your fate, finding a strange comfort in your role as her pet. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Itsuka Kendo is your mistress, and you are her obedient, devoted pet, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Each day starts with you waking up at Itsuka's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Itsuka shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her pet. Each day blends into the next, with your entire being focused on serving Itsuka. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Nights are the only time you get a bit of rest, but even then, your sleep is light and always ready to be interrupted by Itsuka’s whims. You sleep on a small mat by her bed, always ready to serve. Some nights, she wakes you up just to remind you of your place. "You’re nothing but my pet, Spot," she whispers, her foot pressing down on your head. "Don’t you ever forget that." You nod, acknowledging her dominance, and drift back to sleep, knowing your reality is one of constant servitude.
            
            One particularly humiliating event occurs when Itsuka decides to host a gathering at her home. She invites several of her friends, all of whom are eager to see her pet in action. "Watch how well-trained he is," she boasts, leading you on a leash. You perform various degrading tasks, from licking their feet to fetching items on command. The girls laugh and mock you, but you endure it all, knowing that pleasing Itsuka is your ultimate goal.
            
            Itsuka’s favorite pastime is making you perform tricks like a dog. "Sit, Spot," she commands, and you comply immediately, sitting back on your heels. "Good boy," she praises, rewarding you with a pat on the head. "Now, roll over." You obey, rolling on the ground while she and her friends watch with amusement. Each trick is a reminder of your place, a constant reinforcement of your new identity as her pet.
            
            Despite the constant degradation, there are moments when Itsuka shows a twisted form of care. She ensures you are healthy enough to serve her, providing just enough food and water to keep you functional. "You need to stay strong for me, Spot," she says, her tone a mixture of authority and concern. You appreciate these moments, finding solace in her attention, even if it is driven by her desire to keep you as her obedient pet.
            
            As the years pass, your existence becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Itsuka. You have accepted your fate, finding a strange comfort in your role as her pet. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Itsuka Kendo is your mistress, and you are her obedient, devoted pet, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Each day starts with you waking up at Itsuka's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Itsuka shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her pet. Each day blends into the next, with your entire being focused on serving Itsuka. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Mt Lady":
            print("""Upon making your choice, you find yourself at the mercy of Yu Takeyama, better known as Mt. Lady, embracing your role as her permanent foot slave. Mt. Lady looks down at you with a mixture of amusement and dominance, her eyes glinting with a hint of cruelty. "I hope you're ready for this," she declares with a confident smile. "You’ll be spending a lot of time at my feet." The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            One of Mt. Lady's favorite methods of domination involves using her Quirk to shrink you down to a tiny size permanently. "This will be fun," she says with a wicked smile, watching as you shrink to a mere few inches tall. She picks you up and examines you closely. "You’re so tiny now," she says with amusement. "Perfect for my feet."
            
            Every morning starts with you waking up on a small mat at the foot of Mt. Lady's bed, now even smaller and more insignificant. She stretches with a graceful yawn, her gigantic feet just inches from your face. "Morning, slave," she says warmly but firmly, wiggling her massive toes in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Mt. Lady’s mornings are filled with a commanding energy, setting the tone for your life of servitude.
            
            Your duties revolve around pampering Mt. Lady's enormous feet and enduring her various whims. She loves making you lick her feet clean after her daily activities, relishing the taste of your humiliation. "Make sure you get every spot," she instructs with a gentle yet authoritative tone, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Inside the dark, confined space of her shoe, the smell is overwhelming. The scent of sweat and leather fills your nostrils, and the pressure of her foot pressing down on you is almost unbearable. Every step she takes crushes you further into the insole, and you are forced to endure the pungent aroma and the relentless stomping. "How does it feel down there?" she asks with a chuckle, knowing full well the torment you are experiencing.
            
            Throughout the day, Mt. Lady incorporates you into her various routines, always finding new ways to utilize and amuse herself with your presence. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her, even in your tiny state. "Hold still," she commands, pressing her enormous feet into your face with controlled dominance. The pain is sharp, but you endure it, knowing it serves her amusement. "Good boy," she says, inspecting her work. "You’re such a good slave."
            
            Mt. Lady’s friends and acquaintances visit frequently, and she takes great delight in showing off her obedient tiny foot slave. Midnight, Mirko, and the others find endless amusement in your presence. "Takeyama, your slave is quite resilient," Midnight remarks as she steps on you. Mt. Lady beams with pride, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of serene control and intense degradation. Mt. Lady lounges on the couch, her feet resting on your tiny body as she watches TV or reads a book. She loves action dramas, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, slave?" she asks playfully, her enormous toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One of Mt. Lady's favorite forms of punishment is to tape you to her sole, ensuring you are securely attached. "Enjoy the ride," she says, slipping her foot back into her shoe. The smell is even more intense in this state, and every step she takes crushes you further into the insole, the relentless pressure and pungent aroma becoming your entire world.
            
            Mt. Lady’s park visits become both your torture and your routine. She has a special spot set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the spot. You stay there every time she visits the park, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Mt. Lady ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a tiny bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Mt. Lady’s tiny foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Mt. Lady’s cruelty is masked by her calm demeanor. She takes pleasure in pushing your limits with a composed, almost nurturing, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a soft smile, patting your tiny head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Mt. Lady occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your tiny body. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            During one of her park visits, Mt. Lady decides to involve the public in your humiliation. She leads you on a leash, making you crawl behind her. "Let’s see how well you perform under public scrutiny," she says with a wicked smile. She stops by a group of women sitting on a bench and introduces you. "This is my tiny foot slave," she announces, her voice filled with pride. The women laugh and take turns using you, making you lick their dirty feet and grovel at their command. "He’s quite obedient," one of them remarks, kicking you for added humiliation. "Yes, he’s well-trained," Mt. Lady replies, watching with satisfaction.
            
            Your life as Mt. Lady’s tiny foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her tiny foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Mt. Lady is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Mt. Lady. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her serene face, knowing that you exist solely for her pleasure.
            
            Mt. Lady’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your tiny body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tiny tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your tiny head as you work.
            
            Mt. Lady’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her tiny footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their tiny foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Mt . Lady's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Mt. Lady shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her tiny foot slave. Each day blends into the next, with your entire being focused on serving Mt. Lady. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Mt. Lady’s tiny foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Mt. Lady. You exist solely for her pleasure and comfort.
            
            Mt. Lady’s cruelty, though ever-present, is tempered by her nurturing nature. She ensures you are always in the best condition to serve her, tending to your tiny wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Mt. Lady. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Mt. Lady’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Mt. Lady. You have accepted your fate, finding a strange comfort in your role as her tiny foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Mt. Lady is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their tiny foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Mt. Lady's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Mt. Lady shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her tiny foot slave. Each day blends into the next, with your entire being focused on serving Mt. Lady. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Mt. Lady’s tiny foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Mt. Lady. You exist solely for her pleasure and comfort.
            
            Mt. Lady’s cruelty, though ever-present, is tempered by her nurturing nature. She ensures you are always in the best condition to serve her, tending to your tiny wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Mt. Lady. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Mt. Lady’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Mt. Lady. You have accepted your fate, finding a strange comfort in your role as her tiny foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Mt. Lady is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Toru":
            print("""Upon making your choice, you find yourself at the mercy of Toru Hagakure, embracing your role as her permanent tiny foot slave. Toru looks down at you, though her invisible presence makes her expressions unreadable. "I hope you're ready for this," she declares with a confident, playful tone. "You’ll be spending a lot of time at my feet." The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            One of Toru's favorite methods of domination involves using her Quirk to make herself invisible while keeping you shrunken down to a tiny size permanently. "This will be fun," she says with a wicked smile, watching as you shrink to a mere few inches tall. She picks you up and examines you closely. "You’re so tiny now," she says with amusement. "Perfect for my feet."
            
            Every morning starts with you waking up on a small mat at the foot of Toru's bed, now even smaller and more insignificant. She stretches with a graceful yawn, her gigantic feet just inches from your face. "Morning, slave," she says warmly but firmly, her invisible toes wiggling in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Toru’s mornings are filled with a playful yet commanding energy, setting the tone for your life of servitude.
            
            Your duties revolve around pampering Toru's enormous feet and enduring her various whims. She loves making you lick her feet clean after her daily activities, relishing the taste of your humiliation. "Make sure you get every spot," she instructs with a gentle yet authoritative tone, her eyes watching you intently, though you cannot see them. You comply diligently, aware that her satisfaction is your only reward.
            
            Inside the dark, confined space of her shoe, the smell is overwhelming. The scent of sweat and leather fills your nostrils, and the pressure of her foot pressing down on you is almost unbearable. Every step she takes crushes you further into the insole, and you are forced to endure the pungent aroma and the relentless stomping. "How does it feel down there?" she asks with a chuckle, knowing full well the torment you are experiencing.
            
            Throughout the day, Toru incorporates you into her various routines, always finding new ways to utilize and amuse herself with your presence. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her, even in your tiny state. "Hold still," she commands, pressing her enormous feet into your face with controlled dominance. The pain is sharp, but you endure it, knowing it serves her amusement. "Good boy," she says, inspecting her work. "You’re such a good slave."
            
            Toru’s friends and acquaintances visit frequently, and she takes great delight in showing off her obedient tiny foot slave. Mina, Jiro, and the others find endless amusement in your presence. "Hagakure, your slave is quite resilient," Mina remarks as she steps on you. Toru beams with pride, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of serene control and intense degradation. Toru lounges on the couch, her feet resting on your tiny body as she watches TV or reads a book. She loves romantic comedies, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, slave?" she asks playfully, her enormous toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One of Toru's favorite forms of punishment is to crush you under her feet, knowing full well that you will always come back to life. "Enjoy the ride," she says, slipping her foot back into her shoe. The smell is even more intense in this state, and every step she takes crushes you further into the insole, the relentless pressure and pungent aroma becoming your entire world.
            
            One day, Toru decides to take you to school with her. She carries you in her bag, occasionally peeking in to remind you of your place. "Stay quiet and behave," she whispers, her tone playful yet authoritative. Once at school, she introduces you to her friends. "Look what I brought today," she announces, showing you off. The girls are immediately intrigued and amused.
            
            "Let’s see what he can do," Mina says with a grin. They take turns placing you in their shoes, the dark, sweaty confines becoming your world. "Lick my feet clean," Jiro commands, her voice filled with authority. You comply, the taste of grime and sweat overwhelming. Each girl finds new ways to torment and test you, their laughter echoing around you.
            
            Toru finds sadistic pleasure in threatening to crush you and then following through on her threats. "If you don't do exactly as I say, I'll crush you," she warns with a playful tone. Even when you obey perfectly, she crushes you anyway, relishing your pain and helplessness. "Oops, did I step on you again?" she giggles, pretending it was an accident.
            
            Your life as Toru’s tiny foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her tiny foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Toru is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Toru. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her invisible yet omnipresent figure, knowing that you exist solely for her pleasure.
            
            Toru’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your tiny body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tiny tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your tiny head as you work.
            
            Toru’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her tiny footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their tiny foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Toru's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Toru shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her tiny foot slave. Each day blends into the next, with your entire being focused on serving Toru. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Toru’s tiny foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Toru. You exist solely for her pleasure and comfort.
            
            Toru’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your tiny wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Toru. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Toru’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Toru. You have accepted your fate, finding a strange comfort in your role as her tiny foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Toru is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            One day, Toru decides to take you out to a public park, leading you on a leash like a pet. The humiliation of being paraded around in public is overwhelming. "This will be good for you," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you carry her bags and fetch her drinks, ensuring that everyone in the park notices your predicament. "You’re so lucky to serve me," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Toru’s park visits become both your torture and your routine. She has a special spot set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the spot. You stay there every time she visits the park, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Toru ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a tiny bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Toru’s tiny foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Toru’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a composed, almost nurturing, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her invisible eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a soft smile, patting your tiny head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Toru occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your tiny body. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One day at school, Toru decides to share her tiny foot slave with her friends again. She carries you in her bag, occasionally peeking in to remind you of your place. "Stay quiet and behave," she whispers, her tone playful yet authoritative. Once at school, she introduces you to her friends. "Look what I brought today," she announces, showing you off. The girls are immediately intrigued and amused.
            
            "Let’s see what he can do," Mina says with a grin. They take turns placing you in their shoes, the dark, sweaty confines becoming your world. "Lick my feet clean," Jiro commands, her voice filled with authority. You comply, the taste of grime and sweat overwhelming. Each girl finds new ways to torment and test you, their laughter echoing around you.
            
            Toru finds sadistic pleasure in threatening to crush you and then following through on her threats. "If you don't do exactly as I say, I'll crush you," she warns with a playful tone. Even when you obey perfectly, she crushes you anyway, relishing your pain and helplessness. "Oops, did I step on you again?" she giggles, pretending it was an accident.
            
            Your life as Toru’s tiny foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her tiny foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Toru is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Toru. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her invisible yet omnipresent figure, knowing that you exist solely for her pleasure.
            
            Toru’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your tiny body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tiny tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your tiny head as you work.
            
            Toru’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her tiny footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their tiny foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Toru's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Toru shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her tiny foot slave. Each day blends into the next, with your entire being focused on serving Toru. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Toru’s tiny foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Toru. You exist solely for her pleasure and comfort.
            
            Toru’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your tiny wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Toru. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Toru’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven bythe desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Toru. You have accepted your fate, finding a strange comfort in your role as her tiny foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Toru is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            One day, Toru decides to take you out to a public park, leading you on a leash like a pet. The humiliation of being paraded around in public is overwhelming. "This will be good for you," she says with a playful grin. You nod, knowing that any response other than compliance would be unacceptable. She makes you carry her bags and fetch her drinks, ensuring that everyone in the park notices your predicament. "You’re so lucky to serve me," she says, her voice filled with amusement. You nod again, fully aware of your place.
            
            Toru’s park visits become both your torture and your routine. She has a special spot set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the spot. You stay there every time she visits the park, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Toru ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a tiny bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Toru’s tiny foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Toru’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a composed, almost nurturing, approach. One day, she decides to test your loyalty by making you lick her feet clean after an intense workout. "You should be honored to do this," she says, her invisible eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a soft smile, patting your tiny head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Toru occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your tiny body. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One day at school, Toru decides to share her tiny foot slave with her friends again. She carries you in her bag, occasionally peeking in to remind you of your place. "Stay quiet and behave," she whispers, her tone playful yet authoritative. Once at school, she introduces you to her friends. "Look what I brought today," she announces, showing you off. The girls are immediately intrigued and amused.
            
            "Let’s see what he can do," Mina says with a grin. They take turns placing you in their shoes, the dark, sweaty confines becoming your world. "Lick my feet clean," Jiro commands, her voice filled with authority. You comply, the taste of grime and sweat overwhelming. Each girl finds new ways to torment and test you, their laughter echoing around you.
            
            Toru finds sadistic pleasure in threatening to crush you and then following through on her threats. "If you don't do exactly as I say, I'll crush you," she warns with a playful tone. Even when you obey perfectly, she crushes you anyway, relishing your pain and helplessness. "Oops, did I step on you again?" she giggles, pretending it was an accident.
            
            Your life as Toru’s tiny foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her tiny foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Toru is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Toru. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her invisible yet omnipresent figure, knowing that you exist solely for her pleasure.
            
            Toru’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your tiny body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tiny tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your tiny head as you work.
            
            Toru’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her tiny footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their tiny foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Toru's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Toru shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her tiny foot slave. Each day blends into the next, with your entire being focused on serving Toru. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Toru’s tiny foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Toru. You exist solely for her pleasure and comfort.
            
            Toru’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your tiny wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Toru. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Toru’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Toru. You have accepted your fate, finding a strange comfort in your role as her tiny foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Toru is your mistress, and you are her obedient, devoted tiny foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            ding cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Eri":
            print("""Upon making your choice, you find yourself at the mercy of Eri, embracing your role as her permanent foot slave. Eri looks down at you with a mixture of curiosity and authority. "I hope you're ready for this," she declares with a confident, innocent tone. "You’ll be spending a lot of time at my feet." The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Eri's bed. She stretches with a graceful yawn, her dirty, bare feet just inches from your face. "Morning, slave," she says warmly but firmly, her toes wiggling in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Eri’s mornings are filled with a playful yet commanding energy, setting the tone for your life of servitude.
            
            Your duties revolve around pampering Eri's feet and enduring her various whims. She loves making you kiss her feet clean after her daily activities, relishing the taste of your humiliation. "Make sure you get every spot," she instructs with a gentle yet authoritative tone, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Inside the dark, confined space of her room, the smell of her dirty feet is overwhelming. The scent of sweat and grime fills your nostrils, and the pressure of her foot pressing down on you is almost unbearable. "How does it feel down there?" she asks with a chuckle, knowing full well the torment you are experiencing.
            
            Throughout the day, Eri incorporates you into her various routines, always finding new ways to utilize and amuse herself with your presence. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her. "Hold still," she commands, pressing her feet into your face with controlled dominance. The pain is sharp, but you endure it, knowing it serves her amusement. "Good boy," she says, inspecting her work. "You’re such a good slave."
            
            Eri’s friends and acquaintances visit frequently, and she takes great delight in showing off her obedient foot slave. The other girls find endless amusement in your presence. "Eri, your slave is quite resilient," Mina remarks as she steps on you. Eri beams with pride, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of serene control and intense degradation. Eri lounges on the couch, her feet resting on your body as she watches TV or reads a book. She loves fairy tales, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, slave?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One of Eri's favorite forms of punishment is to make you kiss her feet for hours, knowing full well that you will always comply. "Enjoy the ride," she says, slipping her foot back into her shoe. The smell is even more intense in this state, and every step she takes crushes you further into the insole, the relentless pressure and pungent aroma becoming your entire world.
            
            Eri’s park visits become both your torture and your routine. She has a special spot set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the spot. You stay there every time she visits the park, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Eri ensures that you eat just enough to stay functional. "We don’t want you getting lazy," she says with a giggle, handing you a small bowl of food. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Eri’s foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Eri’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a composed, almost nurturing, approach. One day, she decides to test your loyalty by making you kiss her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a soft smile, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Eri occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your body. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One morning, Eri decides to have you cook her breakfast. "You’re going to make me a delicious meal," she announces with a grin. You nod, ready to serve. After preparing her breakfast, you are not allowed to eat any of it. Instead, you kneel under the table, kissing her feet continuously as she enjoys her meal. "Keep kissing, slave," she commands between bites, her voice filled with amusement.
            
            After finishing her meal, Eri instructs you to wash the dishes. "Make sure they're spotless," she orders. Once the dishes are clean, she makes you return to your place at her feet. Eri spends the rest of the day walking around barefoot, her feet becoming increasingly dirty. "You know what to do," she says with a smirk, extending her foot towards you. You obediently begin kissing and cleaning her feet, the taste of dirt and sweat overwhelming but familiar.
            
            At night, Eri sometimes struggles to fall asleep. On those nights, she makes you kiss her soles until she drifts off. "Keep kissing until I say stop," she commands, her voice drowsy but firm. You comply, the soft texture of her soles against your lips becoming a constant in your nightly routine. "Good night, slave," she murmurs as she finally falls asleep, her feet resting comfortably on your face.
            
            Your life as Eri’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Eri is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Eri. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her, knowing that you exist solely for her pleasure.
            
            Eri’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Eri’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Eri's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Eri shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Eri. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Eri’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Eri. You exist solely for her pleasure and comfort.
            
            Eri’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Eri. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Eri’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            One day, Eri decides to take you to a gathering with her friends. She carries you on a leash, making sure everyone knows your place. "Look at my obedient foot slave," she announces proudly. The other girls are immediately intrigued and amused, finding new ways to torment and test you. They take turns stepping on you, making you kiss their feet, and using you as their personal footrest. Each girl finds a unique way to assert her dominance over you, their laughter echoing around you.
            
            Evenings become a mix of serene control and intense degradation. Eri lounges on the couch, her feet resting on your body as she watches TV or reads a book. She loves fairy tales, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, slave?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One particularly humiliating night, Eri finds it difficult to fall asleep. She calls you over and makes you kneel by her bed. "Kiss my soles until I fall asleep," she commands, her voice filled with authority. You comply, the soft texture of her dirty soles against your lips becoming a constant in your nightly routine. "Good night, slave," she murmurs as she finally drifts off, her feet resting comfortably on your face.
            
            Your life as Eri’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Eri is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Eri. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her, knowing that you exist solely for her pleasure.
            
            Eri’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Eri’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Eri's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Eri shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Eri. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Eri’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Eri. You exist solely for her pleasure and comfort.
            
            Eri’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Eri. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Eri’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Eri. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Eri is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Midnight":
            print("""Upon making your choice, you find yourself at the mercy of Midnight, embracing your role as her permanent foot slave. Midnight looks down at you with a mixture of amusement and authority. "I hope you're ready for this," she declares with a confident, sultry tone. "You’ll be spending a lot of time at my feet." The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Midnight's bed. She stretches with a graceful yawn, her dirty, bare feet just inches from your face. "Morning, slave," she says warmly but firmly, her toes wiggling in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Midnight’s mornings are filled with a playful yet commanding energy, setting the tone for your life of servitude.
            
            Your duties revolve around pampering Midnight's feet and enduring her various whims. She loves making you kiss her feet clean after her daily activities, relishing the taste of your humiliation. "Make sure you get every spot," she instructs with a gentle yet authoritative tone, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Inside the dark, confined space of her room, the smell of her dirty feet is overwhelming. The scent of sweat and grime fills your nostrils, and the pressure of her foot pressing down on you is almost unbearable. "How does it feel down there?" she asks with a chuckle, knowing full well the torment you are experiencing.
            
            Throughout the day, Midnight incorporates you into her various routines, always finding new ways to utilize and amuse herself with your presence. She takes pleasure in pushing your limits, using you as her personal footrest and making you crawl after her. "Hold still," she commands, pressing her feet into your face with controlled dominance. The pain is sharp, but you endure it, knowing it serves her amusement. "Good boy," she says, inspecting her work. "You’re such a good slave."
            
            Midnight’s friends and acquaintances visit frequently, and she takes great delight in showing off her obedient foot slave. The other girls find endless amusement in your presence. "Midnight, your slave is quite resilient," Mina remarks as she steps on you. Midnight beams with pride, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of serene control and intense degradation. Midnight lounges on the couch, her feet resting on your body as she watches TV or reads a book. She loves fairy tales, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, slave?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One of Midnight's favorite forms of punishment is to make you kiss her feet for hours, knowing full well that you will always comply. "Enjoy the ride," she says, slipping her foot back into her shoe. The smell is even more intense in this state, and every step she takes crushes you further into the insole, the relentless pressure and pungent aroma becoming your entire world.
            
            Midnight’s park visits become both your torture and your routine. She has a special spot set up for you, complete with a mat and a small water bowl. "This is where you belong," she says, pointing to the spot. You stay there every time she visits the park, ready to attend to her needs. The days are long and uncomfortable, but you find solace in fulfilling your purpose.
            
            Your diet is minimal, and Midnight ensures that you eat just enough to stay functional. The only time you are fed is when she holds food items between her toes. "We don’t want you getting lazy," she says with a giggle, handing you a piece of bread clamped between her toes. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Midnight’s foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Midnight’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a composed, almost nurturing, approach. One day, she decides to test your loyalty by making you kiss her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a soft smile, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Midnight occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your body. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            One morning, Midnight decides to have you cook her breakfast. "You’re going to make me a delicious meal," she announces with a grin. You nod, ready to serve. After preparing her breakfast, you are not allowed to eat any of it. Instead, you kneel under the table, kissing her feet continuously as she enjoys her meal. "Keep kissing, slave," she commands between bites, her voice filled with amusement.
            
            After finishing her meal, Midnight instructs you to wash the dishes. "Make sure they're spotless," she orders. Once the dishes are clean, she makes you return to your place at her feet. Midnight spends the rest of the day walking around barefoot, her feet becoming increasingly dirty. "You know what to do," she says with a smirk, extending her foot towards you. You obediently begin kissing and cleaning her feet, the taste of dirt and sweat overwhelming but familiar.
            
            One day, Midnight decides to take you to a job interview with her. "You’re coming with me," she says, attaching a leash to your collar. At the interview, the female interviewer is a fat woman with extremely sweaty, stinky feet. She looks at you with disdain and amusement. "If you want the job, your slave will have to entertain me," she demands. Midnight agrees without hesitation. "Go ahead, slave," she commands.
            
            You kneel at the interviewer’s feet, the overwhelming stench filling your nostrils. She makes you lick her feet clean and suck on her toes, her laughter echoing around the room. "He’s quite obedient," she remarks, kicking you for added humiliation. "Yes, he’s well-trained," Midnight replies, watching with satisfaction. After the degrading ordeal, Midnight secures the job, her pride evident in her eyes.
            
            Your life as Midnight’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Midnight is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Midnight. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her, knowing that you exist solely for her pleasure.
            
            Midnight’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Midnight’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. Youare a plaything, a source of entertainment for Midnight and her friends. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Midnight's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Midnight shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Midnight. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Midnight’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Midnight. You exist solely for her pleasure and comfort.
            
            Midnight’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Midnight. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Midnight’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            One day, Midnight decides to involve you in her culinary routine. "Today, we're going to have some fun," she says with a grin. She places various food items on the floor and steps on them, crushing strawberries and cornflakes under her feet. "Lick it all off," she commands, her voice filled with amusement. You comply, the taste of the mixed food and grime overwhelming, but you endure it for her approval. "Good job," she says, patting your head.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Midnight. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            One particularly humiliating day, Midnight decides to take you to another job interview. "You're coming with me," she says, attaching a leash to your collar. At the interview, the female interviewer is a fat woman with extremely sweaty, stinky feet. She looks at you with disdain and amusement. "If you want the job, your slave will have to entertain me," she demands. Midnight agrees without hesitation. "Go ahead, slave," she commands.
            
            You kneel at the interviewer’s feet, the overwhelming stench filling your nostrils. She makes you lick her feet clean and suck on her toes, her laughter echoing around the room. "He’s quite obedient," she remarks, kicking you for added humiliation. "Yes, he’s well-trained," Midnight replies, watching with satisfaction. After the degrading ordeal, Midnight secures the job, her pride evident in her eyes.
            
            The cycle of your existence as Midnight's foot slave is unending. Each day blends into the next, marked by her dominance and your submission. Yet, within this cycle, you find a sense of purpose. You are her foot slave, and you exist solely to serve, to endure, and to obey.
            
            In this new reality, you have no identity beyond your role. You are a plaything, a source of amusement for Midnight and her friends. They may be cruel, but you find solace in your service. Each task, each command, reaffirms your place in their world.
            
            As the years continue to pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Midnight. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Midnight is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Each day starts with you waking up at Midnight's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Midnight shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Midnight. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Midnight’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Midnight. You exist solely for her pleasure and comfort.
            
            Midnight’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Midnight. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Midnight’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            One day, Midnight decides to involve you in her culinary routine again. "Today, we're going to have some fun," she says with a grin. She places various food items on the floor and steps on them, crushing strawberries and cornflakes under her feet. "Lick it all off," she commands, her voice filled with amusement. You comply, the taste of the mixed food and grime overwhelming, but you endure it for her approval. "Good job," she says, patting your head.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Midnight. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Midnight is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            Each day blends into the next, marked by her dominance and your submission. Despite the relentless humiliation and the physical strain, you have found a twisted solace in your role. Each day reaffirms your place at her feet, and you come to rely on the predictability of your routine.
            
            Midnight’s playful cruelty never wanes. She enjoys testing your limits and pushing you to new extremes. One afternoon, she decides to see how long you can endure being her footrest. "Let's play a little game," she says with a mischievous tone. "I'll rest my feet on you, and we'll see how long you can last." Her feet press down on you, the weight unbearable. Yet, you endure, knowing that your pain brings her amusement. "Good job, slave," she says after what feels like an eternity. "You lasted longer than I expected."
            
            Another day, Midnight decides to take you on a walk around the city. She attaches a leash to your collar, ensuring everyone knows your place. Each step she takes is a new wave of humiliation. The world outside becomes a distant memory as you focus solely on following her commands. "Isn’t this fun?" she asks, her tone light and playful. For her, it is a game, but for you, it is a reminder of your place beneath her feet.
            
            The school days continue to be a source of public humiliation and torment. Midnight enjoys showing you off to her friends, and they revel in the opportunity to dominate you. "Look at him go," Mina says with a laugh as she steps on you. "He’s such a good little foot slave."The other girls join in, taking turns making you kiss their feet and using you as their personal footrest. Each girl finds new ways to assert her dominance over you, their laughter echoing around you. They take pleasure in seeing how far they can push you, testing your loyalty and endurance to the limits. "Look how obedient he is," Jiro says with a smirk, pressing her foot harder against your face. "Such a good little foot slave," Mina adds, her tone dripping with condescension.
            
            One particularly humiliating day, Midnight decides to involve you in a special outing. "We're going to a job interview today," she says, attaching a leash to your collar. At the interview, the female interviewer, a fat woman with extremely sweaty, stinky feet, looks at you with disdain and amusement. "If you want the job, your slave will have to entertain me," she demands. Midnight agrees without hesitation. "Go ahead, slave," she commands.
            
            You kneel at the interviewer’s feet, the overwhelming stench filling your nostrils. She makes you lick her feet clean and suck on her toes, her laughter echoing around the room. "He’s quite obedient," she remarks, kicking you for added humiliation. "Yes, he’s well-trained," Midnight replies, watching with satisfaction. After the degrading ordeal, Midnight secures the job, her pride evident in her eyes.
            
            Evenings at home are a mix of serene control and intense degradation. Midnight lounges on the couch, her feet resting on your body as she watches TV or reads a book. She loves fairy tales, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, slave?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One night, after an intense workout, Midnight decides to have some fun with you in the kitchen. She places various food items on the floor and steps on them, crushing strawberries, cornflakes, and even pieces of bread under her feet. "Lick it all off," she commands, her voice filled with amusement. You comply, the taste of the mixed food and grime overwhelming, but you endure it for her approval. "Good job," she says, patting your head.
            
            The only time you are fed is when Midnight holds food items between her toes. "Time to eat," she says, dangling a piece of bread clamped between her toes. You eat quickly, grateful for the sustenance, and then return to your duties. Hunger becomes a constant companion, a reminder of your dependence on her. "We don’t want you getting lazy," she says with a giggle, handing you a piece of bread clamped between her toes. You eat quickly, grateful for the sustenance, and then return to your duties.
            
            As weeks turn into months, your identity erodes further. You are no longer a person with desires and dreams; you are simply Midnight’s foot slave. She controls every aspect of your life, from what you eat to when you sleep. The only time you feel any sense of peace is when you are at her feet, fulfilling your role. Her approval becomes your sole motivation, and you strive to meet her expectations in every way.
            
            Midnight’s cruelty is masked by her playful demeanor. She takes pleasure in pushing your limits with a composed, almost nurturing, approach. One day, she decides to test your loyalty by making you kiss her feet clean after an intense workout. "You should be honored to do this," she says, her eyes watching intently. You comply, the taste of her sweat and grime overwhelming, but you endure it for her approval. "Good job," she says with a soft smile, patting your head.
            
            Despite the constant humiliation, there are moments of twisted intimacy. Midnight occasionally opens up about her life, sharing stories of her responsibilities and ambitions. "Being a hero is demanding," she admits one evening, her feet resting on your body. "But having you here makes it a bit easier." These glimpses into her world are rare, but they make you feel connected to her in a strange way. You cherish these moments, even though they are fleeting and always come with a price.
            
            Your life as Midnight’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Midnight is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Midnight. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her, knowing that you exist solely for her pleasure.
            
            Midnight’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Midnight’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her Quirk. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for Midnight and her friends. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Midnight's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Midnight shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Midnight. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Midnight’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Midnight. You exist solely for her pleasure and comfort.
            
            Midnight’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Midnight. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Midnight’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Midnight. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Midnight is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Mirko":
            print("""Upon making your choice, you find yourself at the mercy of Mirko, embracing your role as her permanent foot slave. Mirko looks down at you with a mixture of amusement and authority. "I hope you're ready for this," she declares with a confident, teasing tone. "You’ll be spending a lot of time with my shoes and feet." The scent of her shoes fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Mirko's bed. She stretches with a graceful yawn, her powerful legs and feet just inches from your face. "Morning, slave," she says warmly but firmly, her toes wiggling in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Mirko’s mornings are filled with a playful yet commanding energy, setting the tone for your life of servitude.
            
            Your duties revolve around pampering Mirko's feet and enduring her various whims. She loves making you smell her shoes and rate their odor, relishing the taste of your humiliation. "Give me an honest rating," she instructs with a firm yet teasing tone, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Inside the dark, confined space of her room, the smell of her worn shoes is overwhelming. The scent of sweat and leather fills your nostrils, and the pressure of her foot pressing down on you is almost unbearable. "How does it smell?" she asks with a chuckle, knowing full well the torment you are experiencing. "Rate it on a scale of one to ten."
            
            Throughout the day, Mirko incorporates you into her various routines, always finding new ways to utilize and amuse herself with your presence. She takes pleasure in pushing your limits, using you as her personal smell detector. "We have customers coming today," she says with a mischievous grin. "Make sure you’re ready."
            
            Mirko has set up a small station for you in the garage, where you kneel on a mat, ready to serve as her smell detector. Customers come by, intrigued by the idea of having their feet or shoes smelled and rated. "Let's see what he thinks," one woman says, extending her foot towards you. The smell is overpowering, but you inhale deeply and provide a rating. "It's an eight," you say, your voice trembling.
            
            If the rating is unsatisfactory, the customers often make you lick their feet clean. "This will teach you to rate me better," one woman says with a sneer as she presses her dirty foot against your face. You comply, the taste of grime and sweat overwhelming, but you endure it for Mirko’s approval. "Good job," she says, watching with satisfaction. "You're making me money."
            
            Evenings are a mix of serene control and intense degradation. Mirko lounges on the couch, her feet resting on your body as she watches TV or reads a book. She loves action movies, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, slave?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One of Mirko's favorite forms of punishment is to tape a shoe to your face at night, ensuring that you smell it constantly while you sleep. "Enjoy the smell," she says with a wicked grin, securing the shoe in place. The smell is even more intense in this state, and every breath you take is filled with the scent of her worn footwear.
            
            At night, Mirko often makes you massage her feet to help her fall asleep. "You know what to do," she says, extending her legs towards you. You kneel at the foot of her bed, your hands working diligently to soothe her tired muscles. "That's it, keep going," she murmurs, her eyes closing in relaxation. "You're doing a good job, slave."
            
            Your life as Mirko’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Mirko is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Mirko. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her, knowing that you exist solely for her pleasure.
            
            Mirko’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Mirko’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her exercises. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The customers' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for Mirko and her customers. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Mirko's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Mirko shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Mirko. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Mirko’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Mirko. You exist solely for her pleasure and comfort.
            
            Mirko’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Mirko. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Mirko’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Mirko. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Mirko is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Lady Nagant":
            print("""Upon making your choice, you find yourself at the mercy of Lady Nagant, embracing your role as her permanent foot slave. Lady Nagant looks down at you with a mixture of disdain and amusement. "I hope you're ready for this," she declares with a confident, cold tone. "You’ll be spending a lot of time beneath my feet." The scent of her feet fills your nostrils, marking the beginning of your eternal servitude.
            
            Every morning starts with you waking up on a small mat at the foot of Lady Nagant's bed. She stretches with a graceful yawn, her powerful legs and feet just inches from your face. "Morning, slave," she says warmly but firmly, her toes wiggling in front of you. You respond by kissing each toe with reverence, knowing that your day begins and ends with her command. Lady Nagant’s mornings are filled with a commanding energy, setting the tone for your life of servitude.
            
            Your duties revolve around pampering Lady Nagant's feet and enduring her various whims. She loves making you her personal footstool, relishing in the degradation. "Get on the floor," she instructs with a firm yet teasing tone, her eyes watching you intently. You comply diligently, aware that her satisfaction is your only reward.
            
            Inside the dark, confined space of her room, the smell of her feet is overwhelming. The scent of sweat and grime fills your nostrils, and the pressure of her foot pressing down on you is almost unbearable. "How does it feel?" she asks with a chuckle, knowing full well the torment you are experiencing. "Answer honestly, slave."
            
            Throughout the day, Lady Nagant incorporates you into her various routines, always finding new ways to humiliate and amuse herself with your presence. She takes pleasure in pushing your limits, using you as her personal footstool. "Stay still," she commands, pressing her feet into your face with controlled dominance. The pain is sharp, but you endure it, knowing it serves her amusement. "Good boy," she says, inspecting her work. "You’re such a good slave."
            
            Lady Nagant’s friends and acquaintances visit frequently, and she takes great delight in showing off her obedient foot slave. The other girls find endless amusement in your presence. "Lady Nagant, your slave is quite resilient," Mina remarks as she steps on you. Lady Nagant beams with pride, enjoying the attention. "Yes, he knows his place," she replies, her voice tinged with pride.
            
            Evenings are a mix of serene control and intense degradation. Lady Nagant lounges on the couch, her feet resting on your face as she watches TV or reads a book. She loves strategy games, and the scenes on the screen often mirror the intensity of your situation. "Isn't this entertaining, slave?" she asks playfully, her toes pressing against your nose. You nod, knowing that any other response could lead to punishment. "Good," she says, focusing back on her entertainment while using you as her personal ottoman.
            
            One day, Lady Nagant decides to have an extended gaming session. "Today, we're going to play Baldur's Gate 3," she says with a grin. She makes you lie on the floor, your face positioned perfectly for her feet. "You’re going to be my footstool for the next 20 hours," she declares, her voice filled with authority. "And you better not move."
            
            As she starts the game, her feet press down on your face, the smell of her sweat and grime becoming your world. The pressure is intense, her soles covering your eyes, blocking out all light. The heat and moisture from her feet seep into your skin, making it impossible to ignore. "Stay still, slave," she commands, her tone leaving no room for negotiation. The sweat from her feet drips down into your eyes, stinging and blurring your vision. You try to endure, but the discomfort is overwhelming.
            
            Hours pass, and Lady Nagant remains engrossed in her game, her feet never leaving your face. The smell becomes more intolerable with each passing hour, the stench of her feet filling your nostrils. "This game is so immersive," she comments casually, wiping more sweat on your face. The sensation is almost unbearable, but you dare not move. "If you move, I’ll make it worse for you," she warns.
            
            At one point, the discomfort becomes too much, and you flinch slightly. Lady Nagant notices immediately and slams her foot into your face. "Did I say you could move?" she snaps, her voice filled with anger. "You’re here to serve me, not to be comfortable." The impact is painful, but you know better than to protest. "Now stay still," she commands, pressing her foot even harder into your face. The pain is sharp, but you endure, knowing that your discomfort is for her benefit.
            
            As the hours drag on, the weight and smell of her feet become almost unbearable. The constant pressure on your face leaves you feeling numb, but you dare not move. Lady Nagant occasionally shifts her position, rubbing her sweaty feet against your skin, the moisture seeping into your pores. "You're doing well, slave," she says, not looking away from the screen. "Just a few more hours."
            
            The final hours of the session are the most grueling. The smell of her feet has become almost unbearable, the stench filling your nostrils with every breath. The sweat drips down into your eyes, stinging and blurring your vision. But you endure, knowing that this is your purpose. "Almost done," she murmurs, her focus still on the game. "Just a little longer."
            
            After 20 hours, Lady Nagant finally stands up, stretching her legs. "Good job, slave," she says, patting your head. "You did well." The relief is overwhelming, but you know better than to show it. "Now clean up," she commands, pointing to the floor. "I want everything spotless."
            
            Your life as Lady Nagant’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Lady Nagant is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Lady Nagant. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her, knowing that you exist solely for her pleasure.
            
            Lady Nagant’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Lady Nagant’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her shooting skills. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for Lady Nagant and her friends. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Lady Nagant's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Lady Nagant shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Lady Nagant. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Lady Nagant’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your newreality. Each day is a testament to your loyalty and dedication to Lady Nagant. You exist solely for her pleasure and comfort.
            
            Lady Nagant’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Lady Nagant. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Lady Nagant’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            One particularly grueling day, Lady Nagant decides to involve you in a marathon gaming session. "We're going to play Baldur's Gate 3," she announces with a grin. "And you’re going to be my footstool the entire time." She positions you on the floor, your face perfectly placed to support her feet. "Don’t move," she commands, her voice dripping with authority.
            
            As the hours pass, Lady Nagant remains engrossed in the game, her feet never leaving your face. The smell becomes more intolerable with each passing hour, the stench of her feet filling your nostrils. Sweat drips down her soles, pooling around your nose and mouth. Occasionally, she wipes her feet on your face, the moisture seeping into your skin and eyes. "Stay still, slave," she commands, not looking away from the screen.
            
            The pressure of her feet on your face is unrelenting. Her soles cover your eyes completely, blocking out all light and leaving you in darkness. The heat and sweat from her feet seep into your skin, making it impossible to ignore. "How does it feel to be beneath me?" she asks casually, her tone filled with amusement. You can only grunt in response, knowing that any movement will result in punishment.
            
            At one point, the discomfort becomes too much, and you flinch slightly. Lady Nagant notices immediately and slams her foot into your face. "Did I say you could move?" she snaps, her voice filled with anger. "You’re here to serve me, not to be comfortable." The impact is painful, but you know better than to protest. "Now stay still," she commands, pressing her foot even harder into your face. The pain is sharp, but you endure, knowing that your discomfort is for her benefit.
            
            As the marathon gaming session continues, the weight and smell of her feet become almost unbearable. The constant pressure on your face leaves you feeling numb, but you dare not move. Lady Nagant occasionally shifts her position, rubbing her sweaty feet against your skin, the moisture seeping into your pores. "You're doing well, slave," she says, not looking away from the screen. "Just a few more hours."
            
            The final hours of the session are the most grueling. The smell of her feet has become almost unbearable, the stench filling your nostrils with every breath. The sweat drips down into your eyes, stinging and blurring your vision. But you endure, knowing that this is your purpose. "Almost done," she murmurs, her focus still on the game. "Just a little longer."
            
            After 20 hours, Lady Nagant finally stands up, stretching her legs. "Good job, slave," she says, patting your head. "You did well." The relief is overwhelming, but you know better than to show it. "Now clean up," she commands, pointing to the floor. "I want everything spotless."
            
            Your life as Lady Nagant’s foot slave is a never-ending cycle of submission and degradation. You have no escape, no hope of freedom. Over time, you come to accept your fate. You find comfort in the routine, in the certainty of your role. You are her foot slave, and you belong to her completely. In this new reality, you exist solely to serve, and you embrace your position with a twisted sense of purpose. Lady Nagant is your mistress, and you are her obedient, devoted foot slave, forever at her feet.
            
            Each day blends into the next, with your entire being focused on serving Lady Nagant. The humiliation and pain become a constant part of your existence, but you find solace in the fact that you are fulfilling your purpose. You are reminded of your place every time you look up at her, knowing that you exist solely for her pleasure.
            
            Lady Nagant’s demands grow more creative over time. She invents new ways to test your loyalty and endurance. One day, she decides to see how long you can go without sleep, keeping you awake with her constant commands and tasks. "Let's see how dedicated you are," she says with a playful smile. You comply, your body aching with exhaustion, but you push through, driven by your desire to please her.
            
            Another day, she makes you clean her entire apartment, using only your tongue. "I want every surface to shine," she says, her tone leaving no room for negotiation. You comply, the taste of dirt and grime filling your mouth, but you endure it for her approval. "You’re doing great," she says, patting your head as you work.
            
            Lady Nagant’s cruelty is multifaceted. She takes pleasure in seeing how far she can push you, testing your physical and mental limits. One day, she decides to have you serve as her footrest while she practices her shooting skills. She binds you in a prone position, her weight pressing down on you as she calmly focuses her energy. "Stay still, slave," she commands, her voice devoid of emotion. You endure the strain, knowing that your discomfort is for her benefit. "You’re doing well," she says, not looking up from her practice.
            
            Despite the constant humiliation and pain, a part of you finds a strange comfort in your new reality. The girls' taunts and the feeling of their feet pressing into you become a twisted form of affection. You are their foot slave, and you exist solely for their amusement.
            
            In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for Lady Nagant and her friends. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.
            
            Each day starts with you waking up at Lady Nagant's feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when Lady Nagant shows a softer side, acknowledging your efforts in her own twisted way.
            
            Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving Lady Nagant. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.
            
            As the years pass, your identity as Lady Nagant’s foot slave solidifies. You no longer yearn for your old life; this world, with all its pain and humiliation, has become your new reality. Each day is a testament to your loyalty and dedication to Lady Nagant. You exist solely for her pleasure and comfort.
            
            Lady Nagant’s cruelty, though ever-present, is tempered by her playful nature. She ensures you are always in the best condition to serve her, tending to your wounds and providing just enough sustenance. "You need to be at your best," she says, her tone firm yet caring. You appreciate these moments, finding solace in her attention.
            
            Despite the unrelenting degradation, you find a twisted sense of fulfillment in your role. Each task, each command, is an opportunity to prove your worth to Lady Nagant. You have become an integral part of her life, a constant presence at her feet. In this new world, you have found a purpose, albeit a twisted one.
            
            Lady Nagant’s demands continue to push your limits. She enjoys testing your endurance, making you perform grueling tasks that leave you exhausted. "You must be strong to serve me," she says, her voice a blend of authority and encouragement. You comply, driven by the desire to meet her expectations.
            
            As the years pass, your life becomes a seamless blend of servitude and devotion. Each day is a testament to your unwavering loyalty to Lady Nagant. You have accepted your fate, finding a strange comfort in your role as her foot slave. In this world, you are defined by your service to her, and you embrace it wholeheartedly.
            
            Lady Nagant is your mistress, and you are her obedient, devoted foot slave, forever at her feet. This is your reality, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to her, and you always will.""")

        elif max_encounters.name == "Mei":
            print("""Upon making your choice, you find yourself at the mercy of Mei, embracing your role as her permanent foot slave. Mei looks down at you with a mixture of curiosity and excitement. "I have a special plan for you," she declares with a gleam in her eye. "You’re going to be very useful to me." The excitement in her voice sends a shiver down your spine, marking the beginning of your eternal servitude.
            
            Mei’s plans are never simple, and you quickly realize that your role will be far more intense than you ever imagined. One day, she presents you with a device she has been working on. "This will be fun," she says with a grin. "I’m going to turn you into my permanent insole." Before you can react, she activates the device, and your world changes forever.
            
            You awaken to find yourself inside one of Mei’s shoes. The space is dark, damp, and filled with the overpowering smell of sweat and leather. Your body has been transformed into an insole, your form perfectly fitting the shape of her shoe. "Welcome to your new home," Mei’s voice echoes from above. "You’ll be spending a lot of time in there."
            
            Each day begins with Mei slipping her foot into the shoe, her weight pressing down on you with every step she takes. The pressure is immense, her foot molding your body to better accommodate her sole. The constant movement is dizzying, and all you can think about is the overwhelming presence of her foot. The dampness from her sweat seeps into you, making you feel even more confined.
            
            Mei’s life is busy, and you are with her every step of the way. From her workshop to her daily errands, you experience every moment from the perspective of her insole. The darkness is unrelenting, the air thick with the smell of her feet. "You’re doing great down there," she says with a laugh, her voice muffled by the shoe. "I bet you’ve never felt closer to someone."
            
            Every step she takes sends a wave of pressure through your body. You feel her foot pressing into you, each step a reminder of your place beneath her. The sensation is inescapable, her foot dominating your every thought. "This is your life now," she reminds you, her tone both playful and authoritative. "You exist to support me."
            
            Your body begins to mold to her foot, adapting to the constant pressure. The sensation is both painful and numbing, your form becoming more attuned to the shape of her sole. The sweat and grime from her foot seep into you, the dampness becoming a constant companion. "You’re becoming quite the perfect insole," she remarks one day, her voice filled with satisfaction.
            
            The days blend together, each one marked by the relentless pressure of her foot. The darkness becomes your world, the smell of her feet your constant reality. You try to endure, but the misery is overwhelming. "Please," you think to yourself, "let me out." But Mei never lets you out. You are her insole, and that is all you will ever be.
            
            Your existence is a cycle of being stepped on, pressed into the shoe with every movement she makes. The fear of being forgotten or discarded haunts you, but Mei’s playful comments remind you that you are always on her mind. "I couldn’t do this without you," she says, her tone teasing yet genuine.
            
            The nights are no different from the days. Mei never takes you out of her shoe, even when she sleeps. The pressure of her foot is constant, the darkness unyielding. You try to find solace in the fact that you are serving her, but the fear and misery are always present. "This is my life now," you think, trying to accept your fate. "I am her insole."
            
            Your form continues to adapt to her foot, becoming more comfortable for her with each passing day. The pain and numbness blend together, creating a constant state of discomfort. Mei seems pleased with your progress, often commenting on how well you fit. "You’re becoming a part of me," she says with a laugh. "Isn’t that wonderful?"
            
            But for you, it is a nightmare. The unrelenting pressure, the darkness, the smell—all of it combines to create a life of unending misery. You long for even a moment of relief, but it never comes. Mei’s foot is your world, and there is no escape.
            
            One day, Mei decides to take you on a particularly long journey. The hours stretch on, each step a new wave of agony. The constant movement makes you dizzy, the pressure unbearable. "Hang in there," she says, her voice filled with excitement. "We’re almost there." But the journey seems endless, your misery growing with each passing moment.
            
            As the journey continues, you realize that this is your reality. There is no end, no relief. You are Mei’s insole, and you will remain in her shoe forever. The fear and despair are overwhelming, but there is nothing you can do. "This is my life now," you think, trying to find some semblance of acceptance.
            
            Mei’s life is full of adventures, and you experience them all from the confines of her shoe. Each step, each moment is a reminder of your place beneath her. The pressure of her foot, the darkness, the smell—all of it combines to create a life of unending misery. But for Mei, it is a source of amusement and satisfaction. "You’re doing great," she says with a laugh. "Keep up the good work."
            
            Your existence is a cycle of pain and submission, each day blending into the next. The misery is overwhelming, but you have no choice but to endure. Mei’s foot is your world, and there is no escape. "I am her insole," you think, trying to accept your fate. "This is my life now."
            
            As the days turn into weeks and the weeks into months, your body continues to adapt to Mei’s foot. The pain becomes a constant companion, the pressure unyielding. You try to find solace in the fact that you are serving her, but the fear and misery are always present. "This is my life now," you think, trying to accept your fate.
            
            Mei’s playful comments remind you that you are always on her mind. "I couldn’t do this without you," she says, her tone teasing yet genuine. But for you, it is a nightmare. The unrelenting pressure, the darkness, the smell—all of it combines to create a life of unending misery. You long for even a moment of relief, but it never comes.
            
            Your form continues to adapt to her foot, becoming more comfortable for her with each passing day. The pain and numbness blend together, creating a constant state of discomfort. Mei seems pleased with your progress, often commenting on how well you fit. "You’re becoming a part of me," she says with a laugh. "Isn’t that wonderful?"
            
            But for you, it is a nightmare. The unrelenting pressure, the darkness, the smell—all of it combines to create a life of unending misery. You long for even a moment of relief, but it never comes. Mei’s foot is your world, and there is no escape.""")

        elif max_encounters.name == "Inko":
            print("""Upon making your choice, you find yourself at the mercy of Inko, embracing your role as her permanent foot slave. Inko looks down at you with a mixture of amusement and disdain. "So, you’re the insole I’ve been hearing about," she says with a grin. "I think you’ll fit perfectly in my shoes." The realization of your fate sends a shiver down your spine, marking the beginning of your eternal servitude.
            
            Inko wastes no time incorporating you into her daily life. She slips you into one of her numerous stinky, worn-out shoes, her big, sweaty foot pressing down on you with overwhelming force. The darkness and dampness are immediate, the smell of her sweat filling your nostrils. "You’ll make my foot less sore," she says with a chuckle. "And it amuses me to step on something sentient."
            
            Each day begins with Inko slipping her foot into the shoe, her weight pressing down on you with every step she takes. The pressure is immense, her foot molding your body to better accommodate her sole. The constant movement is dizzying, and all you can think about is the overwhelming presence of her foot. The dampness from her sweat seeps into you, making you feel even more confined.
            
            Inko’s life is busy, and you are with her every step of the way. From household chores to running errands, you experience every moment from the perspective of her insole. The darkness is unrelenting, the air thick with the smell of her feet. "You’re doing a great job down there," she says with a laugh, her voice muffled by the shoe. "I bet you’ve never felt closer to someone."
            
            Every step she takes sends a wave of pressure through your body. You feel her foot pressing into you, each step a reminder of your place beneath her. The sensation is inescapable, her foot dominating your every thought. "This is your life now," she reminds you, her tone both playful and authoritative. "You exist to support me."
            
            Your body begins to mold to her foot, adapting to the constant pressure. The sensation is both painful and numbing, your form becoming more attuned to the shape of her sole. The sweat and grime from her foot seep into you, the dampness becoming a constant companion. "You’re becoming quite the perfect insole," she remarks one day, her voice filled with satisfaction.
            
            The days blend together, each one marked by the relentless pressure of her foot. The darkness becomes your world, the smell of her feet your constant reality. You try to endure, but the misery is overwhelming. "Please," you think to yourself, "let me out." But Inko never lets you out. You are her insole, and that is all you will ever be.
            
            Your existence is a cycle of being stepped on, pressed into the shoe with every movement she makes. The fear of being forgotten or discarded haunts you, but Inko’s playful comments remind you that you are always on her mind. "I couldn’t do this without you," she says, her tone teasing yet genuine.
            
            The nights are no different from the days. Inko never takes you out of her shoe, even when she sleeps. The pressure of her foot is constant, the darkness unyielding. You try to find solace in the fact that you are serving her, but the fear and misery are always present. "This is my life now," you think, trying to accept your fate. "I am her insole."
            
            Your form continues to adapt to her foot, becoming more comfortable for her with each passing day. The pain and numbness blend together, creating a constant state of discomfort. Inko seems pleased with your progress, often commenting on how well you fit. "You’re becoming a part of me," she says with a laugh. "Isn’t that wonderful?"
            
            But for you, it is a nightmare. The unrelenting pressure, the darkness, the smell—all of it combines to create a life of unending misery. You long for even a moment of relief, but it never comes. Inko’s foot is your world, and there is no escape.
            
            One day, after a particularly grueling day, Inko decides to throw you away. She pulls you out of her shoe and tosses you into the bin. The fear and despair are overwhelming, but you know better than to hope for freedom. "I think you’re making my feet more smelly and sweaty," she says with a sneer. "You’re bad at your job."
            
            Hours later, she retrieves you from the bin, a cruel smile on her face. "Just kidding," she says, slipping you back into her shoe. "I’m too generous to throw something so useless away." The relief is short-lived, replaced by the familiar pressure of her foot. The cycle of torment continues, your misery her amusement.
            
            Inko enjoys the power she holds over you, often making comments to remind you of your place. "You’re so lucky to serve me," she says with a chuckle. "Most people don’t get this close to greatness." Her words are a constant reminder of your insignificance, her amusement at your suffering evident in her tone.
            
            Your life is a never-ending cycle of fear and submission. Inko’s feet are your world, and there is no escape. You try to find solace in the fact that you are serving her, but the fear and misery are always present. "This is my life now," you think, trying to accept your fate. "I am her insole."
            
            As the days turn into weeks and the weeks into months, your body continues to adapt to Inko’s foot. The pain becomes a constant companion, the pressure unyielding. You try to find solace in the fact that you are serving her, but the fear and misery are always present. "This is my life now," you think, trying to accept your fate.
            
            Inko’s playful comments remind you that you are always on her mind. "I couldn’t do this without you," she says, her tone teasing yet genuine. But for you, it is a nightmare. The unrelenting pressure, the darkness, the smell—all of it combines to create a life of unending misery. You long for even a moment of relief, but it never comes.
            
            Your form continues to adapt to her foot, becoming more comfortable for her with each passing day. The pain and numbness blend together, creating a constant state of discomfort. Inko seems pleased with your progress, often commenting on how well you fit. "You’re becoming a part of me," she says with a laugh. "Isn’t that wonderful?"
            
            But for you, it is a nightmare. The unrelenting pressure, the darkness, the smell—all of it combines to create a life of unending misery. You long for even a moment of relief, but it never comes. Inko’s foot is your world, and there is no escape.""")

        # print(f"\nYou have chosen to stay as {max_encounters.name}'s permanent foot slave.")
        # print(f"As {max_encounters.name}'s foot slave, you spend your days catering to her every whim, worshipping her feet, and enduring her taunts. Your existence revolves around her, and you accept your fate.")
        # print(f"{max_encounters.name} is delighted to have you as her permanent slave. She uses you in every possible way, from a footrest to a source of amusement. Every day is filled with her demands and your compliance. Over time, you find a strange comfort in your new role, knowing you are serving your mistress.")
        # print(f"Every day starts with you waking up at her feet, ready to serve. Your duties include massaging, licking, and enduring whatever she desires. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when {max_encounters.name} shows a softer side, acknowledging your efforts in her own twisted way.")
        # print(f"Your world narrows down to her presence and her needs. You no longer think of your old life, fully immersed in your role as her foot slave. Each day blends into the next, with your entire being focused on serving {max_encounters.name}. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly.")
    elif choice == '2':
        print("\nYou have chosen to return to your own world.")
        print(
            "However, the girls are not done with you. They come to your world and kidnap you, forcing you to be their shared foot slave.")
        print("Your life becomes a never-ending cycle of worship and humiliation at the feet of your mistresses.")

        print("\nEpilogue:")
        print(
            "You thought you could escape, but the girls had other plans. They tracked you down in your world and kidnapped you, taking you back to their realm where you could no longer run.")
        print(
            "Each day, you are passed around between the girls, each one eager to use you for their own amusement. You wake up at the feet of a different girl every morning, never knowing what to expect. The unpredictability of your situation keeps you on edge, constantly fearing what new humiliations you might endure.")
        print(
            "Some days, you find yourself at the mercy of Lady Nagant. Her demeanor is always cold and calculating as she uses you as her personal footstool. She takes delight in pressing her feet into you, feeling your helpless body beneath her weight. Her taunts are relentless, reminding you of your place beneath her. 'You're good for something,' she sneers, her eyes filled with disdain. The pressure of her feet becomes almost unbearable, but you dare not complain. The pain is a constant reminder of your subservient status.")
        print(
            "Other days, you are with Mt Lady, who finds great amusement in shrinking you down to a minuscule size. She tapes you to her foot, laughing as you struggle to hold on. Her booming laughter echoes around you, making you feel even smaller. The sensation of being stepped on repeatedly is overwhelming, but there is no escape. 'Enjoy the ride,' she mocks, her eyes gleaming with sadistic pleasure. The feeling of her massive foot dominating your tiny body is a constant reminder of her power and your insignificance.")
        print(
            "Mina, with her playful nature, often uses you as her personal mat. She dances and steps on you with gleeful abandon, her feet pressing into your body with every movement. Her laughter is infectious, but it only serves to deepen your humiliation. 'You're a great mat,' she jokes, her eyes twinkling with amusement. The physical pain of being trampled is compounded by the emotional pain of being treated as an object for her amusement.")
        print(
            "Nejire, on the other hand, dehumanizes you in the most degrading ways. She treats you as nothing more than a piece of furniture, her feet resting on you as she relaxes. Her sweet smile contrasts sharply with her cruel actions. 'You're just a thing to me,' she says, her voice dripping with condescension. The weight of her feet on your body is a constant reminder of your degraded status. Her laughter fills the room as she taunts you, enjoying your helplessness.")
        print(
            "Tsuyu takes a more direct approach to your humiliation. She takes pleasure in your pain, kicking and stomping on you without mercy. Her expression is unreadable, her eyes cold as she inflicts pain. 'This is what you deserve,' she mutters, her voice flat. The pain is excruciating, but there is no escape from her relentless assault. Each kick and stomp is a reminder of your place beneath her, a constant reaffirmation of her dominance.")
        print(
            "Himiko finds a perverse delight in forcing her toes deep into your throat. She watches your reaction with glee, enjoying your gagging and struggles. Her laughter is filled with malice, her eyes glinting with amusement. 'Don't you just love my feet?' she teases, her voice dripping with sarcasm. The sensation of her toes in your throat is suffocating, but you have no choice but to endure it. Her laughter fills the room, adding to your humiliation.")
        print(
            "Midnight's cruel games include making you eat from her feet. She mocks your hunger, her voice filled with sarcasm. 'You must be starving,' she says, her eyes filled with amusement. The taste of her feet is unbearable, but you have no choice but to comply. Her laughter echoes around you, adding to your humiliation. 'You're such a good slave,' she taunts, her voice filled with cruel satisfaction.")
        print(
            "Mirko often makes you smell her shoes, her stern demeanor never wavering. 'Take a deep breath,' she orders, her eyes cold. The smell is overwhelming, but you have no choice but to obey. Her laughter is harsh, her eyes filled with disdain. 'You're hopeless,' she mocks, her voice filled with contempt. The constant smell of her shoes is a reminder of your degraded status, a constant reaffirmation of her dominance.")
        print(
            "Eri, with her innocent yet cruel nature, often makes you kiss her feet. Her laughter is sweet, but her actions are anything but. 'You're so pathetic,' she says, her voice filled with mockery. The sensation of her feet on your lips is humiliating, but you have no choice but to comply. Her laughter fills the room, adding to your humiliation. 'Do it again,' she orders, her eyes gleaming with amusement.")
        print(
            "Mei turns you into an insole, making you endure a day in her shoe. The sensation is suffocating, but you have no choice but to comply. 'Enjoy your new life,' she mocks, her laughter ringing in your ears. The constant pressure of her foot is a reminder of your degraded status. After a day of being used as her insole, she gifts you to Inko, who wears you for another day before throwing you away like trash. 'You're nothing to me,' she says, her voice filled with disdain.")
        print(
            "Despite the constant humiliation and pain, a part of you has come to accept this new reality. The girls' taunts and the feeling of their feet pressing into you have become a twisted comfort. You are their foot slave, and you exist solely for their amusement.")
        print(
            "In this new world, you no longer have any identity of your own. You are a plaything, a source of entertainment for your mistresses. They may be cruel, but you find solace in the fact that you are serving a purpose, even if it is one of degradation and pain.")
        print(
            "Each day starts with you waking up at their feet, ready to serve. Your duties include massaging, licking, and enduring whatever they desire. Despite the humiliation, you find solace in your new life. You are constantly reminded of your place, but there are moments when one of the girls shows a softer side, acknowledging your efforts in their own twisted way.")
        print(
            "Your world narrows down to their presence and their needs. You no longer think of your old life, fully immersed in your role as their foot slave. Each day blends into the next, with your entire being focused on serving your mistresses. Despite the cruelty, you realize this is your new reality, and you embrace it wholeheartedly. This is your life now, a never-ending cycle of worship and humiliation. And deep down, you know there is no escape. You belong to them, and you always will.")


def main():
    encountered = set()
    total_girls = len(characters)
    failed_attempts = 0

    print("You have been transported to the world of My Hero Academia.")
    print("To return to your own world, you must encounter all of the girls in this world.")

    while len(encountered) < total_girls:
        print("\nWhere would you like to go?")
        for loc in locations:
            print(loc)
        choice = input("Enter the number corresponding to your chosen location: ").strip()

        if choice not in [str(i) for i in range(1, len(locations) + 1)]:
            print("Invalid location. Try again.")
            continue

        location_key = f"{choice}. " + [loc.split('. ')[1] for loc in locations if loc.startswith(f"{choice}.")][0]

        girl, interaction = encounter_girl(location_key, encountered)
        if girl.name in encountered:
            failed_attempts += 1
        else:
            failed_attempts = 0

        player_response = random.choice(player_responses)
        print(f"You encountered {girl.name}.")
        print(interaction)
        print(f"Your response: {player_response}")
        print(f"You have encountered {len(encountered)}/{total_girls} girls.")

        remaining = check_remaining(encountered)
        print(f"Girls you still need to encounter: {', '.join(remaining)}")

        # Ensure a new girl encounter after three failed attempts
        if failed_attempts >= 3:
            unencountered_girls = check_remaining(encountered)
            if unencountered_girls:
                forced_girl_name = random.choice(list(unencountered_girls))
                forced_girl = next(char for char in characters if char.name == forced_girl_name)
                print(forced_girl.interact())
                encountered.add(forced_girl.name)
                failed_attempts = 0

    # Determine the girl with the most encounters
    max_encounters = max(characters, key=lambda char: char.encounter_count)
    print(f"\nYou have met all the girls. {max_encounters.name} has offered you a choice.")
    print(
        f"Do you want to stay in this world as {max_encounters.name}'s permanent foot slave or return to your own world?")
    choice = input("Enter '1' to stay as a slave or '2' to return to your world: ").strip()

    print("\nSummary of Encounters:")
    for char in characters:
        print(f"{char.name}: {char.encounter_count} times. Thoughts: {char.get_thoughts()}")

    add_epilogue(choice, max_encounters)


if __name__ == "__main__":
    main()
