from willie import module

# NOTE: You *HAVE* to use one {0} in each string - this gets replaced by the nick
phrases = [
	"You need to shut up, {0}",
	"{0}: Well done. Here come the test results: You are a horrible person. I'm serious, that's what it says: A horrible person. We weren't even testing for that.",
	"{0}: You're not just a regular moron. You were DESIGNED to be a moron."
]
counter = 0

@module.rule("^.*(shut)(up)(glados).*$")
@module.rule("^.*(fuck)(you)(glados).*$")
def shut_up(bot, trigger):
	global phrases
	global counter
	bot.say(phrases[counter].format(trigger.nick))
	counter = (counter + 1) % len(phrases)

