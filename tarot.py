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
print("I can give you a Tarot reading based on your Past, Present and Future.\n")
# Ask users permission to give a reading
def give_reading():
    reading_prompt = input("Would you like a reading today? y/n  ")
    if reading_prompt == "y":
        print("Wonderful!  Let's see what the cards can tell you today")
        # Call past_reading function
    elif reading_prompt == "n":
        print("No problem.  Come back anytime to get your reading.") 
    else:
        print("Please type either 'y' or 'n'.")
        return give_reading()

print(give_reading())   

# Class for tarot cards
class Card:
    def __init__(self, upright_meaning, reversed_meaning):
        self.upright_meaning = upright_meaning
        self.reversed_meaning = reversed_meaning

# Dictionary for tarot cards
tarot_cards = {
    "The Fool": Card("New opportunities and beginnings are available to you. Be open-minded and curious, ready to explore and discover new things. Play, have fun, and be spontaneous.",
                    "You have conceived of a new project but aren't ready to \"birth\" it just yet. You are worried about the risks and fear the unknown."),
    "The Magician": Card("You are taking action to manifest your goals and have the resources to create what you desire. You combine magic and practicality to bring your ideas to reality.",
                        "You are discovering what you wish to manifest without taking action just yet. You are uncertain if you have the tools you need; let the Universe work out the \"how\" while you focus on the \"what\"."),
    "The High Priestess": Card("You are intune with your intuition and your Higher Self.  The answers you seek lie within.  Access your inner wisdom and divine feminine energy.",
                               "let go of ego and fear, and learn to trust your intuition.  Go within and listen to your inner voice."),
    "The Empress": Card("Abundance and creativity flows to you.  You embody the mother archetype and are bringing a new project into being. Your divine feminine energy flows through you as you grow and nuture your \"babies\".",
                        "Connect with your feminine energy and be proud of what you can create when you tap into this power source.  Reaffirm your beauty, inside and out."),
    "The Emperor": Card("You are establishing structures and foundations from which your success will grow.  You favour stability and certainty over flexibility and change.  You have the discipline to see your plans through.",
                        "Step up, be accountable, and get the work done.  Be mindful of your relationship with power and authority - allow this energy to flow through you, not against you."),
    "The Hierophant": Card("You are working with a teacher, mentor, or guiding authority.  You will expand your knowledge and learn fundemental principles with a trusted source",
                           "You are yor own teacher.  The wisdom you seek comes from within, not from an outside source.  you do not need external approval to be successful."),
    "The Lovers": Card("You have a beautiful, soul-honouring connection with another.  You successfully integrate dual forces into a unified state.  You face a choice of the highest moral grounds.",
                       "Honor and love your beautiful self.  Integrate the different parts of yourself to find true alignment and harmony.  Become aware of what you value and honour those values in your choices."),
    "The Chariot": Card("You are a driving force, fuelled by determination and willpower.  You stop at nothing on your path to success.  You overcome obstacles and find cohesion between opposing forces.",
                        "Connect with your inner strength and willpower to move forward.  Your motivation comes from within, not from an external force.  You cannot control everything - sometimes it is best to loosen your grip."),
    "Strength": Card("You have inner power and strength, and lead using subtle influence and persuasion.  You understand your animal instincts and express your raw power with courage and measured restraint.",
                     "You are a powerful force - you just need to connect with this inner power in a constructive way.  Others may question your strength, but you are fierce inside."),


}

# Call for each card
fool_card = tarot_cards["The Fool"]
upright_meaning = fool_card.upright_meaning
reversed_meaning = fool_card.reversed_meaning

magician_card = tarot_cards["The Magician"]
upright_meaning = magician_card.upright_meaning
reversed_meaning = magician_card.reversed_meaning

high_priestess_card = tarot_cards["The High Priestess"]
upright_meaning = high_priestess_card.upright_meaning
reversed_meaning = high_priestess_card.reversed_meaning

empress_card = tarot_cards["The Empress"]
upright_meaning = empress_card.upright_meaning
reversed_meaning = empress_card.reversed_meaning

emperor_card = tarot_cards["The Emperor"]
upright_meaning = emperor_card.upright_meaning
reversed_meaning = emperor_card.reversed_meaning

hierophant_card = tarot_cards["The Hierophant"]
upright_meaning = hierophant_card.upright_meaning
reversed_meaning = hierophant_card.reversed_meaning

lovers_card = tarot_cards["The Lovers"]
upright_meaning = lovers_card.upright_meaning
reversed_meaning = lovers_card.reversed_meaning

chariot_card = tarot_cards["The Chariot"]
upright_meaning = chariot_card.upright_meaning
reversed_meaning = chariot_card.reversed_meaning

strength_card = tarot_cards["Strength"]
upright_meaning = strength_card.upright_meaning
reversed_meaning = strength_card.reversed_meaning


# Make past_reading function

# Make present_reading function

# Make future_reading function

# Give farewell message
