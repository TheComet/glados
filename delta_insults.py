from willie import module

chill_out_counter = 0
chill_out = ["Woahhh, chill the fuck out bro", "Says the guy with two gay daddies", "That was uncalled for"]

@module.rule("^.*what i thought*.$")
def what_i_thought(bot, trigger):
	bot.say(trigger.nick + ": Oh yeah? Think again")

@module.rule("^(?=.*according)(?=.*book).*$")
def according_to_books(bot, trigger):
	bot.say(trigger.nick + ": Just because you read lots of books doesn't mean mommy loves you")

@module.rule("^(?=.*fucking)(?=.*queer).*$")
def fucking_queer_defense(bot, trigger):
	global chill_out
	global chill_out_counter
	bot.say(trigger.nick + ": " + chill_out[chill_out_counter])
	chill_out_counter = (chill_out_counter + 1) % len(chill_out)

@module.rule("^(((?=.*goddammit).*)|((?=.*goddamnit).*)|((?=.*goddangit).*)).*$")
def allah_dammit(bot, trigger):
        bot.say(trigger.nick + ": Allah dammit!")
