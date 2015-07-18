from willie import module

@module.commands("burn")
def burn_user(bot, trigger):
    if not trigger.group(2):
        bot.reply(".burn <user>")
        return
    bot.say(trigger.group(2) + ": OOOOOOOH YOU JUST GOT BURNED, SON")
    bot.say(trigger.nick + ": 1")
    bot.say(trigger.group(2) + ": 0")
