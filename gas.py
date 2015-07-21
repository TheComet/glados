from willie import module

@module.commands("gas")
def gas(bot, trigger):
    if not trigger.group(2):
        bot.say("Ab ins gas du Jude!")
    else:
        bot.say(trigger.group(2) + ": Ab ins gas du Jude!")

