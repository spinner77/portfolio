
import sys
import random
# Welcome ascii art and message
print("""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |      __      | || |  _______     | || |     ____     | || |  _________   | |
| | |  _   _  |  | || |     /  \     | || | |_   __ \    | || |   .'    `.   | || | |  _   _  |  | |
| | |_/ | | \_|  | || |    / /\ \    | || |   | |__) |   | || |  /  .--.  \  | || | |_/ | | \_|  | |
| |     | |      | || |   / ____ \   | || |   |  __ /    | || |  | |    | |  | || |     | |      | |
| |    _| |_     | || | _/ /    \ \_ | || |  _| |  \ \_  | || |  \  `--'  /  | || |    _| |_     | |
| |   |_____|    | || ||____|  |____|| || | |____| |___| | || |   `.____.'   | || |   |_____|    | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""")

print("Welcome Friend.\n")
print("I can give you a Tarot reading based on your Past, Present and Future.")
# Ask users permission to give a reading
def give_reading():
    while True:
        reading_prompt = input("Would you like a reading today? y/n  ").lower()
        if reading_prompt in ["y", "yes"]:
            print("Wonderful!  Let's see what the cards can tell you today")
            return True
        elif reading_prompt in ["n", "no"]:
            print("No problem.  Please feel free to come back anytime you would like a Tarot reading")
            return False
        else:
            print("Sorry, I didn't understand that response. Please enter 'y' or 'n'.")

if give_reading():
    user_name = input("What is your name? ")
    print(f"Thankyou {user_name}, here is your personalised tarot reading.")
else:
    sys.exit(1)  

# Class for tarot cards
class Card:
    def __init__(self, name, upright_meaning, reversed_meaning):
        self.name = name
        self.upright_meaning = upright_meaning
        self.reversed_meaning = reversed_meaning

    def __str__(self):
        return f"Card Name: {self.name}\nCard Meanings:\nUpright: {self.upright_meaning}\nReversed: {self.reversed_meaning}"

    def draw(self):
        orientations = ["upright", "reversed"]
        self.orientation = random.choice(orientations)

    def get_meaning(self):
        return self.upright_meaning if self.orientation == "upright" else self.reversed_meaning

# Dictionary for tarot cards
tarot_cards = {
    "The Fool": Card("The Fool", "New opportunities and beginnings are available to you. Be open-minded and curious, ready to explore and discover new things. Play, have fun, and be spontaneous.",
                    "You have conceived of a new project but aren't ready to \"birth\" it just yet. You are worried about the risks and fear the unknown."),
    "The Magician": Card("The Magician", "You are taking action to manifest your goals and have the resources to create what you desire. You combine magic and practicality to bring your ideas to reality.",
                        "You are discovering what you wish to manifest without taking action just yet. You are uncertain if you have the tools you need; let the Universe work out the \"how\" while you focus on the \"what\"."),
    "The High Priestess": Card("The High Priestess", "You are intune with your intuition and your Higher Self.  The answers you seek lie within.  Access your inner wisdom and divine feminine energy.",
                               "let go of ego and fear, and learn to trust your intuition.  Go within and listen to your inner voice."),
    "The Empress": Card("The Empress", "Abundance and creativity flows to you.  You embody the mother archetype and are bringing a new project into being. Your divine feminine energy flows through you as you grow and nuture your \"babies\".",
                        "Connect with your feminine energy and be proud of what you can create when you tap into this power source.  Reaffirm your beauty, inside and out."),
    "The Emperor": Card("The Emperor", "You are establishing structures and foundations from which your success will grow.  You favour stability and certainty over flexibility and change.  You have the discipline to see your plans through.",
                        "Step up, be accountable, and get the work done.  Be mindful of your relationship with power and authority - allow this energy to flow through you, not against you."),
    "The Hierophant": Card("The Hierophant", "You are working with a teacher, mentor, or guiding authority.  You will expand your knowledge and learn fundemental principles with a trusted source",
                           "You are yor own teacher.  The wisdom you seek comes from within, not from an outside source.  you do not need external approval to be successful."),
    "The Lovers": Card("The Lovers", "You have a beautiful, soul-honouring connection with another.  You successfully integrate dual forces into a unified state.  You face a choice of the highest moral grounds.",
                       "Honor and love your beautiful self.  Integrate the different parts of yourself to find true alignment and harmony.  Become aware of what you value and honour those values in your choices."),
    "The Chariot": Card("The Chariot", "You are a driving force, fuelled by determination and willpower.  You stop at nothing on your path to success.  You overcome obstacles and find cohesion between opposing forces.",
                        "Connect with your inner strength and willpower to move forward.  Your motivation comes from within, not from an external force.  You cannot control everything - sometimes it is best to loosen your grip."),
    "Strength": Card("Strength", "You have inner power and strength, and lead using subtle influence and persuasion.  You understand your animal instincts and express your raw power with courage and measured restraint.",
                     "You are a powerful force - you just need to connect with this inner power in a constructive way.  Others may question your strength, but you are fierce inside."),
    "The Hermit": Card("The Hermit", "You are on a path of spiritual knowledge and self-discovery.  Retreat from everyday life and create space for introspection.  Go within and you'll discover the knowledge and clarity you seek.",
                        "If you feel lost or confused, go within.  Trust that your path will become clear when you connect with yourself on a soul level.  Be careful not to get lost in a deeply spiritual path, disconnecting from the outer world."),
    "Wheel of Fortune": Card("Wheel of Fortune", "You are experiencing the cycle of change.  The wheel is turning and your situation is constantly evolving and shifting.  What goes up must come down and vice versa.",
                             "It may feel as if life is happening to you, not for you, and that you are always running into bad luck.  But you have a choice - you can be at cause or you can be at effect."),
    "Justice": Card("Justice", "You understand cause and effect, and that your choices have consequences.  You seek to equalise and balance, finding the fairest outcome for all.",
                    "Your idea of truth is distorted.  Look at each situation from mulitple angles to uncover the real truth.  Forgive yourself for any misguided decisions you have made."),
    "The Hanged Man": Card("The Hanged Man", "Life is on hold and you are in a state of temporary suspension as you await new insight and clarity.  Step back and look at life from a different perspective.",
                           "If you are feeling stuch and in limbo, surrender to the process.  Trust that this period of pause is for your Highest Good.  What new perspectives are becoming visible to you?"),
    "Death": Card("Death", "You are going through a powerful transformation.  There are parts of your life that are falling away and disinterdrating, making way for new opportunities to emerge.",
                  "You are experiencing deep inner change, letting go of an aspect of yourself that is no longer serving you and making way for something greater.  Do not resist change."),
    "Temperance": Card("Temperance","You are discovering how to create balance and harmony in your life.  You find alignment and a sense of peace with your external surroundings.",
                       "Center yourself and come back into alignment with who you really are.  Focus on your own inner peace, not what's going on around you."),
    "The Devil": Card("The Devil", "You are aware of unhealthy attachments, addictions, and dependencies that are affecting you.  You may think it is hard to let go, but it is easier than you realise.  Let go of fear.",
                      "Be aware of self-sabotage and self-destructive behaviours.  Release any self-imposed limiting beliefs that are standing in the way of your growth and expansion."),
    "The Tower": Card("The Tower", "What you thought were solid foundations are crashing around you.  Destruction and chaos are rampant.  Know that these events are happening \"for\" you, not \"to\" you.  New paradigms and opportunities are emerging.",
                      "Do not resist change.  Even if you see this change as unwanted, it is important to let it run its course.  The change is serving an important purpose and creating the opportunity for deep transformation."),
    "The Star": Card("The Star", "This is a powerful time for inspired action, channelled through your authentic self.  Be open to possibility and stay true to yourself.  Have faith and trust in the Universe, and you will share in its gifts and blessings.",
                     "You lack faith in yourself and the Universe.  Go within to reconnect with your inner source of inspiration and guidance, rather than looking for signs outside of yourself."),
    "The Moon": Card("The Moon", "Connect with your intuition and subconcious mind.  You are experiencing the subtle forces of nature, especially the lunar cycles.  Allow yourself yo flow with these energies.",
                     "You are diving into the murky depths of your innermost mind.  There may be fear, anxiety, and confusion.  You need to go deeper, to the core of your emotions, to release this fear - then you will be free."),
    "The Sun": Card("The Sun", "You are surrounded by warmth, radiance, and vitality.  You are lit up, energised by possibility, growth, and success.  Radiate your light and shine it on the world.",
                    "You may feel depleted or exhausted.  Retreat from the outer world to reenergise and recharge.  You do not have to be \"on\" one hundred percent of the time.  Give yourself a break."),
    "Judgement": Card("Judgement", "This is your time to rise up!  You are experiencing a huge spiritual awakening and realising that you are destined for so much more.  This is your cosmic uplevelling!  Be ready to tune into a higher frequency.",
                      "You may be troubled by your past actions and choices and their consequences for the present.  Self-doubt and judgement are holding you back.  You are so close to a major shift - you just need to get out of your own way."),
    "The World": Card("The World", "You have come full circle and are celebrating the successful completion of an important project or phase.  As you close one chapter, you open another.",
                      "There are many open loops right now and they are draining your energy.  Find closure and tie up loose ends.  Resolve your inner desire for completion, rather than seeking closure with others.")


}

# Function to shuffle and draw the cards
def draw_cards(tarot_cards):
    import random

    card_keys = list(tarot_cards.keys())
    random.shuffle(card_keys)  # Shuffle the keys to ensure randomness

    # Draw three different cards
    past_card = tarot_cards[card_keys.pop()]
    present_card = tarot_cards[card_keys.pop()]
    future_card = tarot_cards[card_keys.pop()]

    # Set orientation for each card
    past_card.draw()
    present_card.draw()
    future_card.draw()

    return past_card, present_card, future_card

# Function to print out the meanings
def print_meanings(past_card, present_card, future_card):
    print("\nPast:")
    print(f"Card: {past_card.name} ({'Upright' if past_card.orientation == 'upright' else 'Reversed'})")
    print(past_card.get_meaning())

    print("\nPresent:")
    print(f"Card: {present_card.name} ({'Upright' if present_card.orientation == 'upright' else 'Reversed'})")
    print(present_card.get_meaning())

    print("\nFuture:")
    print(f"Card: {future_card.name} ({'Upright' if future_card.orientation == 'upright' else 'Reversed'})")
    print(future_card.get_meaning())

# Draw cards and print their meanings
past_card, present_card, future_card = draw_cards(tarot_cards)
print_meanings(past_card, present_card, future_card)

print()    
print(f"Take care {user_name}, and remember this program is for entertainment purposes only.  The readings provided are not a substitute for professional advice and should not be used as such. The information presented in this program is not intended to diagnose, treat, or cure any medical, psychological, or financial conditions. Please use your own discretion when interpreting the cards and their meanings. The creator and contributors of this program are not responsible for any actions taken based on the information provided in the readings. By using this program, you agree to take full responsibility for your own decisions and actions.\n")
