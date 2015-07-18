import willie.module
import codecs
import os.path
import random

def configure(config):
  if config.option('Configure quotes', False):
    config.interactive_add('quotes', 'quotes_data_path', "Path to where you'd like the user quotes to be stored (should be an absolute path to an existing directory).")

def setup(willie):
  global quotes_data_path
  quotes_data_path = willie.config.quotes.quotes_data_path

  if not quotes_data_path.endswith('/'):
    quotes_data_path = quotes_data_path + '/'

def check_nickname_valid(nickname, bot):
  if nickname is None:
    bot.reply("Must pass a nickname as an argument")
    return False

  if not os.path.isfile(quotes_file_name(nickname)):
    bot.reply("I don't know any quotes from %s" % (nickname))
    return False

  return True

def quotes_file_name(nickname):
  return quotes_data_path + nickname + '.txt'

@willie.module.rule("^(.*)$")
def record(bot, trigger):
  quotes_file = codecs.open(quotes_file_name(trigger.nick), 'a', encoding='utf-8')
  quotes_file.write(trigger.group(1) + "\n")
  quotes_file.close

@willie.module.commands('quote')
def quote(bot, trigger):
  nickname = trigger.group(3)

  if not check_nickname_valid(nickname, bot):
    return

  quotes_file = codecs.open(quotes_file_name(nickname), 'r', encoding='utf-8')
  lines = quotes_file.readlines()

  lines = [x for x in lines if len(x) >= 20]

  if len(lines) > 0:
    line = random.choice(lines)
    bot.say("%s once said: \"%s\"" % (nickname, line))

@willie.module.commands('quotestats')
def quotestats(bot, trigger):
  nickname = trigger.group(3)

  if not check_nickname_valid(nickname, bot):
    return

  quotes_file = codecs.open(quotes_file_name(nickname), 'r', encoding='utf-8')
  lines = quotes_file.readlines()

  average_length = float(sum([len(x) for x in lines])) / float(len(lines))

  bot.say("I know about %i quotes from %s" % (len(lines), nickname))
  bot.say("The average quote length is %.2f characters" % (average_length))
