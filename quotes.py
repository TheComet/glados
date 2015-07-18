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

@willie.module.rule("^(.{20,})$")
def record(bot, trigger):
  quotes_file = codecs.open(quotes_data_path + trigger.nick + '.txt', 'a', encoding='utf-8')
  quotes_file.write(trigger.group(1) + "\n")
  quotes_file.close

@willie.module.commands('quote')
def quote(bot, trigger):
  nickname = trigger.group(3)

  if nickname is None:
    return bot.reply("Must pass a nickname as an argument")

  quotes_file_name = quotes_data_path + nickname + '.txt'

  if not os.path.isfile(quotes_file_name):
    return bot.reply("I don't know any quotes from %s" % (nickname))

  quotes_file = codecs.open(quotes_file_name, 'r', encoding='utf-8')
  lines = quotes_file.readlines()

  line = random.choice(lines)
  bot.say("%s once said: \"%s\"" % (nickname, line))
