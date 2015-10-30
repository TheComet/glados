# this requires the showip command line tool
# https://github.com/TheComet93/showip

from willie import module
import commands

@module.commands('showip')
def showip(bot, trigger):
    hostname = trigger.group(2)
    ret = commands.getoutput("/usr/local/bin/showip " + hostname)
    bot.say(ret)

