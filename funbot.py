import random

from errbot import BotPlugin, botcmd


class FunBot(BotPlugin):
    """
    Have fun with your Errbot.
    """

    @botcmd(split_args_with=None)
    def random(self, mess, args):
        """get a random number between min and max

        If only one arg is given it is assumed to be max and min is set to 1.
        """

        if not args or len(args) > 2:
            return u'usage: !random [min max|max]'

        if len(args) == 2:
            min, max = args
        else:
            min = 1
            max = args[0]

        try:
            randint = str(random.randint(int(min), int(max)))
        except ValueError:
            return u'I can only handle numbers.'

        if mess.type == 'groupchat':
            return u'{0} rolls {1} ({2} - {3})'.format(mess.nick, randint, min,
                                                       max)
        else:
            return u'{0} ({1} - {2})'.format(randint, min, max)
