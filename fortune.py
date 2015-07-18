from willie import module

import commands

@module.commands('fortune')
def fortune(bot, trigger):
	fortune = commands.getoutput('fortune')
	for line in fortune.rsplit("\n"):
		bot.say(line)
