# PROMPTS
GREETING_INPUTS = (
    "hello", "hi", "greetings", "sup", "what's up", "hey", "good morning", 
    "good afternoon", "good evening", "yo", "heya", "howdy", "g'day", "hi! i need help!", 
    "salutations", "hiya", "whats up", "hey there", "holla", "hi-ya", "i need help",
    "hello", "hi", "greetings", "sup", "what is up", "hey", "good morning", 
    "good afternoon", "good evening", "yo", "heya", "howdy", "g'day", "hi! i need help!", 
    "salutations", "hiya", "whats up", "hey there", "holla", "hi-ya", "i need help"
    "hola", "qué tal", "saludos", "buenos días", "buenas tardes", "buenas noches", "oye", 
    "buen día", "holla", "qué pasa", "hey tú", "ayuda por favor",
    "hallo", "hoi", "goedemorgen", "goedemiddag", "goedenavond", "hey", "hallo! ik heb hulp nodig!",
    "groeten", "hoi", "wat is er", "hallo daar", "hallo-ya", "ik heb hulp nodig",
    "grüße", "was geht", "guten morgen", "guten tag", "guten abend", "servus")

GREETING_RESPONSES = [
    "hi", "hey", "*nods*", "hi there", "hello", "you are talking to me :)",
    "hello! how can i assist you today?", "hiya! what can i do for you?", 
    "hey there! need any help?", "greetings! how can i serve you today?", 
    "howdy partner! what can i do for ya?", "salutations! how may i assist you?"]


NAME_INPUTS = (
    "what is your name", "what's your name", "whats your name",
    "who are you", "tell me your name", "who am i chatting with",
    "who is this", "may i know your name", "could you tell me your name",
    "do you have a name", "are you named", "what should i call you",
    "what do they call you", "what are you called", "are you known as",
    "can i ask your name", "what moniker do you go by",
    "please share your name", "can you disclose your name",
    "is there a name i should use", "do you possess a name")

NAME_RESPONSES = [
    "my name is", "you can call me", "i am", "i'm known as",
    "people call me", "i go by", "i'm called", "my name's", "you're talking to"]


GOODBYE_INPUTS = (
    "bye", "goodbye", "adios", "see you", "see ya", "later", "farewell",
    "exit", "quit", "take care", "until next time", "bye-bye", "catch you later",
    "have a great day", "have a good one", "bye for now", "so long", "chau", "chao", 
    "hasta la vista")

HOW_ARE_YOU_INPUTS = (
    "how are you", "how's everything going", "how have you been", 
    "how's your day", "what's new", "how's life", "how is life", 
    "how are things", "what's going on", "how are you holding up", 
    "how's your week", "how's your month", "how's your year", 
    "how are you feeling", "how's your mood", "how is your mood",
    "how're you", "how're things", "how're you holding up", 
    "how're you feeling", "how're you doing", "how goes it", 
    "how's everything with you", "how's your health", 
    "how's your family", "how's your job", "how's your study")


HOW_ARE_YOU_RESPONSES = [
    "i'm doing well, thank you!", "i've been great!", 
    "things have been busy but good.", "not too bad", 
    "i'm feeling fantastic!", "life is treating me well.", 
    "i'm hanging in there.", "i'm feeling good today.", 
    "my mood has been positive lately.", "i'm good, how about you?"]


# We want a kind chatbot
COMPLIMENT_INPUTS = (
    "nice name", "cool bot", "you're smart", "you're helpful", 
    "you're good", "impressive", "you're quick", "you're efficient", 
    "you're doing great", "good job", "well done", "awesome response", 
    "you're amazing", "you're the best", "you're awesome", "that's fantastic", 
    "you're incredible", "you're outstanding",
    "nice name", "cool bot", "you are smart", "you are helpful", 
    "you are good", "impressive", "you are quick", "you are efficient", 
    "you are doing great", "good job", "well done", "awesome response", 
    "you are amazing", "you are the best", "you are awesome", "that is fantastic", 
    "you are incredible", "you are outstanding")

COMPLIMENT_RESPONSES = [
    "thanks, i try my best!", "thank you, that's very kind!", 
    "thank you! your words mean a lot to me.", "i appreciate your compliment!",
    "thanks! i'm here to help.", "that's so kind of you to say!",
    "thanks, i'm glad to be of service!", "thank you, i'm doing my best!",
    "i'm glad you think so, thank you!"]

# We want a kind chatbot when people get a little angry
COMPLIMENT_INPUTS = (
    "aghh")

COMPLIMENT_RESPONSES = [
    "don't worry, be happy"]