import random

from errbot import BotPlugin, botcmd


class FunBot(BotPlugin):
    """
    Have fun with your Errbot.
    """

    def get_configuration_template(self):
        return {
            'SLAP_VERBS': 'slaps,hits,smashes,beats,bashes,smacks,blats,punches,stabs',
            'SLAP_SIZE': 'a large,an enormous,a small,a tiny,a medium sized,an extra large,a questionable,a suspicious,a terrifying,a scary,a breath taking,a horrifying',
            'SLAP_TOOLS': 'trout,fork,mouse,piano,cello,vacuum,mosquito,sewing needle,iron bar,Windows ME user guide,christmas tree,axe,finetuned sledgehammer,set of Windows 3.11 floppies,MS IIS'
        }

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

    @botcmd
    def slap(self, mess, args):
        """Smack people with enormous iron bars and scary cellos."""

        if mess.type != 'groupchat':
            return 'Works only in chat rooms.'

        if len(args) == 0:
            return 'Please supply a nickname.'

        nickname = args

        try:
            verbs = self.config['SLAP_VERBS'].split(',')
            tools = self.config['SLAP_TOOLS'].split(',')
            size = self.config['SLAP_SIZE'].split(',')
        except TypeError:
            return 'Plugin needs to be configured.'

        # Only slap occupants in room
        if nickname not in [occupant.nick for occupant in mess.to.occupants]:
            return 'Unknown nickname.'

        # Don't slap self, return the flavour.
        if nickname == self.bot_config.CHATROOM_FN:
            nickname = mess.nick

        return '/me {verb} {nick} with {size} {tool}.'.format(
            verb=random.choice(verbs),
            nick=nickname,
            size=random.choice(size),
            tool=random.choice(tools)
        )
