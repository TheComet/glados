from willie import module
from willie import web
import re

@module.rule(".*(http://pastebin.com/).*")
def java_pastebin(bot, trigger):
	text = trigger.group(1)
	if text:
		tmp = trigger.raw.split("/")
		if len(tmp) >= 3:
			idStr = tmp[3]
			page = web.get("http://pastebin.com/%s" % (idStr))
			re_mark = re.compile('syntax: <a href="/archive/(.*)">.*</a>')
			results = re_mark.findall(page)
			if results:
				if results[0] == "java":
					bot.say("OMG that's a Java code, my eyes!")