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
    "The Hermit": Card("You are on a path of spiritual knowledge and self-discovery.  Retreat from everyday life and create space for introspection.  Go within and you'll discover the knowledge and clarity you seek.",
                        "If you feel lost or confused, go within.  Trust that your path will become clear when you connect with yourself on a soul level.  Be careful not to get lost in a deeply spiritual path, disconnecting from the outer world."),
    "Wheel of Fortune": Card("You are experiencing the cycle of change.  The wheel is turning and your situation is constantly evolving and shifting.  What goes up must come down and vice versa.",
                             "It may feel as if life is happening to you, not for you, and that you are always running into bad luck.  But you have a choice - you can be at cause or you can be at effect."),
    "Justice": Card("You understand cause and effect, and that your choices have consequences.  You seek to equalise and balance, finding the fairest outcome for all.",
                    "Your idea of truth is distorted.  Look at each situation from mulitple angles to uncover the real truth.  Forgive yourself for any ,isguided decisions you have made."),
    "The Hanged Man": Card("Life is on hold and you are in a state of temporary suspension as you await new insight and clarity.  Step back and look at life from a different perspective.",
                           "If you are feeling stuch and in limbo, surrender to the process.  Trust that this period of pause is for your Highest Good.  What new perspectives are becoming visible to you?"),
    "Death": Card("You are going through a powerful transformation.  There are parts of your life that are falling away and disinterdrating, making way for new opportunities to emerge.",
                  "You are experiencing deep inner change, letting go of an aspect of yourself that is no longer serving you and making way for something greater.  Do not resist change."),
    "Temperance": Card("You are discovering how to create balance and harmony in your life.  You find alignment and a sense of peace with your external surroundings.",
                       "Center yourself and come back into alignment with who you really are.  Focus on your own inner peace, not what's going on around you."),
    "The Devil": Card("You are aware of unhealthy attachments, addictions, and dependencies that are affecting you.  You may think it is hard to let go, but it is easier than you realise.  Let go of fear.",
                      "Be aware of self-sabotage and self-destructive behaviours.  Release any self-imposed limiting beliefs that are standing in the way of your growth and expansion."),
    "The Tower": Card("What you thought were solid foundations are crashing around you.  Destruction and chaos are rampant.  Know that these events are happening \"for\" you, not \"to\" you.  New paradigms and opportunities are emerging.",
                      "Do not resist change.  Even if you see this change as unwanted, it is important to let it run its course.  The change is serving an important purpose and creating the opportunity for deep transformation."),
    "The Star": Card("This is a powerful time for inspired action, channelled through your authentic self.  Be open to possibility and stay true to yourself.  Have faith and trust in the Universe, and you will share in its gifts and blessings.",
                     "You lack faith in yourself and the Universe.  Go within to reconnect with your inner source of inspiration and guidance, rather than looking for signs outside of yourself."),
    "The Moon": Card("Connect with your intuition and subconcious mind.  You are experiencing the subtle forces of nature, especially the lunar cycles.  Allow yourself yo flow with these energies.",
                     "You are diving into the murky depths of your innermost mind.  There may be fear, anxiety, and confusion.  You need to go deeper, to the core of your emotions, to release this fear - then you will be free."),
    "The Sun": Card("You are surrounded by warmth, radiance, and vitality.  You are lit up, energised by possibility, growth, and success.  Radiate your light and shine it on the world.",
                    "You may feel depleted or exhausted.  Retreat from the outer world to reenergise and recharge.  You do not have to be \"on\" one hundred percent of the time.  Give yourself a break."),
    "Judgement": Card("This is your time to rise up!  You are experiencing a huge spiritual awakening and realising that you are destined for so much more.  This is your cosmic uplevelling!  Be ready to tune into a higher frequency.",
                      "You may be troubled by your past actions and choices and their consequences for the present.  Self-doubt and judgement are holding you back.  You are so close to a major shift - you just need to get out of your own way."),
    "The World": Card("You have come full circle and are celebrating the successful completion of an important project or phase.  As you close one chapter, you open another.",
                      "There are many open loops right now and they are draining your energy.  Find closure and tie up loose ends.  Resolve your inner desire for completion, rather than seeking closure with others.")


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

hermit_card = tarot_cards["The Hermit"]
upright_meaning = hermit_card.upright_meaning
reversed_meaning = hermit_card.reversed_meaning

wheel_of_fortune_card = tarot_cards["Wheel of Fortune"]
upright_meaning = wheel_of_fortune_card.upright_meaning
reversed_meaning = wheel_of_fortune_card.reversed_meaning

justice_card = tarot_cards["Justice"]
upright_meaning = justice_card.upright_meaning
reversed_meaning = justice_card.reversed_meaning

hanged_man_card = tarot_cards["The Hanged Man"]
upright_meaning = hanged_man_card.upright_meaning
reversed_meaning = hanged_man_card.reversed_meaning

death_card = tarot_cards["Death"]
upright_meaning = death_card.upright_meaning
reversed_meaning = death_card.reversed_meaning

temperance_card = tarot_cards["Temperance"]
upright_meaning = temperance_card.upright_meaning
reversed_meaning = temperance_card.reversed_meaning

devil_card = tarot_cards["The Devil"]
upright_meaning = devil_card.upright_meaning
reversed_meaning = devil_card.reversed_meaning

tower_card = tarot_cards["The Tower"]
upright_meaning = tower_card.upright_meaning
reversed_meaning = tower_card.reversed_meaning

star_card = tarot_cards["The Star"]
upright_meaning = star_card.upright_meaning
reversed_meaning = star_card.reversed_meaning

moon_card = tarot_cards["The Moon"]
upright_meaning = moon_card.upright_meaning
reversed_meaning = moon_card.reversed_meaning

sun_card = tarot_cards["The Sun"]
upright_meaning = sun_card.upright_meaning
reversed_meaning = sun_card.reversed_meaning

judgement_card = tarot_cards["Judgement"]
upright_meaning = judgement_card.upright_meaning
reversed_meaning = judgement_card.reversed_meaning

world_card = tarot_cards["The World"]
upright_meaning = world_card.upright_meaning
reversed_meaning = world_card.reversed_meaning

# Make past_reading function

# Make present_reading function

# Make future_reading function

# Give farewell message
