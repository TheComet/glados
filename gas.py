from willie import module

@module.commands("gas")
def gas(bot, trigger):
    if not trigger.group(2):
        bot.say("Ab ins gas du Jude!")
    else:
        if trigger.group(2).lower()  == "glados":
            bot.say("Nice try. Get comfortable while I warm up the neurotoxin emitters.")
        else:
            bot.say(trigger.group(2) + ": Ab ins gas du Jude!")

