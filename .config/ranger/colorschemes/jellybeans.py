from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class base(ColorScheme):
    progress_bar_color = 1

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.container:
                fg = 1
            if context.directory:
                fg = 4
            elif context.executable and not \
                    any((context.media, context.container,
                       context.fifo, context.socket)):
                fg = 1
            if context.socket:
                fg = 2
            if context.fifo or context.device:
                fg = 0
            if context.link:
                fg = 5
            if context.bad:
                fg = 0
            if context.tag_marker and not context.selected:
                if fg in (7, 8):
                    fg = 1
                else:
                    fg = 1
            if not context.selected and (context.cut or context.copied):
                fg = 15
                bg = 8
            if context.main_column:
                if context.marked:
                    attr |= bold
                    fg = 8
            if context.badinfo:
                if attr & reverse:
                    bg = 1
                else:
                    fg = 7

        elif context.in_titlebar:
            if context.hostname:
                fg = 183
            elif context.directory:
                fg = 110
            elif context.tab:
                fg = 1
            elif context.link:
                fg = 8

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = 7
                elif context.bad:
                    fg = 8
            if context.marked:
                attr |= bold | reverse
                fg = 8
            if context.message:
                if context.bad:
                    fg = 10
            if context.loaded:
                bg = self.progress_bar_color
            if context.vcsinfo:
                fg = 10
                attr &= ~bold
            if context.vcscommit:
                fg = 5
                attr &= ~bold


        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = 8

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color


        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = 11
            elif context.vcschanged:
                fg = 12
            elif context.vcsunknown:
                fg = 210
            elif context.vcsstaged:
                fg = 216
            elif context.vcssync:
                fg = 113
            elif context.vcsignored:
                fg = 141

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync:
                fg = 12
            elif context.vcsbehind:
                fg = 13
            elif context.vcsahead:
                fg = 9
            elif context.vcsdiverged:
                fg = 10
            elif context.vcsunknown:
                fg = 11

        return fg, bg, attr
