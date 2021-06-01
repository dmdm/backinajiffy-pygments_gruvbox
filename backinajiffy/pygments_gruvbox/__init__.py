"""
    backinajiffy.pygments_gruvbox
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Gruvbox by morhetz

    A Pygments style for the Gruvbox themes (licensed under MIT).
    See: https://github.com/morhetz/gruvbox

    :copyright: Copyright 2021 by Dirk Makowski.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Generic, Keyword, Name, Number, \
    Operator, String, Token


GRUVBOX_CONTRAST_LIGHT = ''
GRUVBOX_CONTRAST_DARK = ''


def make_style(colors):
    return {
        Token:                colors['fg0'],

        Comment:              'italic ' + colors['gray'],
        Comment.Hashbang:     colors['gray'],
        Comment.Multiline:    colors['gray'],
        Comment.Preproc:      'noitalic ' + colors['purple'],
        Comment.PreprocFile:  'noitalic ' + colors['gray'],

        Keyword:              colors['red'],
        Keyword.Constant:     colors['purple'],
        Keyword.Declaration:  colors['aqua'],
        Keyword.Namespace:    colors['orange'],
        Keyword.Type:         colors['yellow'],

        Operator:             colors['fg1'],
        Operator.Word:        colors['green'],

        Name.Builtin:         colors['blue'],
        Name.Builtin.Pseudo:  colors['blue'],
        Name.Class:           colors['blue'],
        Name.Constant:        colors['blue'],
        Name.Decorator:       colors['blue'],
        Name.Entity:          colors['blue'],
        Name.Exception:       colors['blue'],
        Name.Function:        'bold ' + colors['blue'],
        Name.Function.Magic:  colors['blue'],
        Name.Label:           colors['blue'],
        Name.Namespace:       colors['blue'],
        Name.Tag:             colors['blue'],
        Name.Variable:        colors['blue'],
        Name.Variable.Global: colors['blue'],
        Name.Variable.Magic:  colors['blue'],

        String:               'italic ' + colors['green'],
        String.Doc:           colors['fg1'],
        String.Regex:         colors['orange'],

        Number:               colors['aqua'],

        Generic:              colors['fg0'],
        Generic.Deleted:      colors['fg3'],
        Generic.Emph:         'italic',
        Generic.Error:        colors['red'],
        Generic.Heading:      'bold',
        Generic.Subheading:   'underline',
        Generic.Inserted:     colors['green'],
        Generic.Output:       colors['fg0'],
        Generic.Prompt:       'bold ' + colors['blue'],
        Generic.Strong:       'bold',
        Generic.Traceback:    colors['blue'],

        Error:                'bg:' + colors['red'],
    }


PALETTE = {
    'dark0-hard':     '#1d2021',
    'dark0':          '#282828',
    'dark0-soft':     '#32302f',
    'dark1':          '#3c3836',
    'dark2':          '#504945',
    'dark3':          '#665c54',
    'dark4':          '#7c6f64',
    'dark4-256':      '#7c6f64',

    'gray-245':       '#928374',
    'gray-244':       '#928374',

    'light0-hard':    '#f9f5d7',
    'light0':         '#fbf1c7',
    'light0-soft':    '#f2e5bc',
    'light1':         '#ebdbb2',
    'light2':         '#d5c4a1',
    'light3':         '#bdae93',
    'light4':         '#a89984',
    'light4-256':     '#a89984',

    'bright-red':     '#fb4934',
    'bright-green':   '#b8bb26',
    'bright-yellow':  '#fabd2f',
    'bright-blue':    '#83a598',
    'bright-purple':  '#d3869b',
    'bright-aqua':    '#8ec07c',
    'bright-orange':  '#fe8019',

    'neutral-red':    '#cc241d',
    'neutral-green':  '#98971a',
    'neutral-yellow': '#d79921',
    'neutral-blue':   '#458588',
    'neutral-purple': '#b16286',
    'neutral-aqua':   '#689d6a',
    'neutral-orange': '#d65d0e',

    'faded-red':      '#9d0006',
    'faded-green':    '#79740e',
    'faded-yellow':   '#b57614',
    'faded-blue':     '#076678',
    'faded-purple':   '#8f3f71',
    'faded-aqua':     '#427b58',
    'faded-orange':   '#af3a03',
}


GB_DARK_BG0 = {
    'soft': PALETTE['dark0-soft'],
    'hard': PALETTE['dark0-hard']
}

DARK_COLORS = {
    'bg0':     GB_DARK_BG0.get(GRUVBOX_CONTRAST_LIGHT, PALETTE['dark0']),
    'bg1':     PALETTE['dark1'],
    'bg2':     PALETTE['dark2'],
    'bg3':     PALETTE['dark3'],
    'bg4':     PALETTE['dark4'],

    'gray':    PALETTE['gray-245'],

    'fg0':     PALETTE['light0'],
    'fg1':     PALETTE['light1'],
    'fg2':     PALETTE['light2'],
    'fg3':     PALETTE['light3'],
    'fg4':     PALETTE['light4'],

    'fg4-256': PALETTE['light4-256'],

    'red':     PALETTE['bright-red'],
    'green':   PALETTE['bright-green'],
    'yellow':  PALETTE['bright-yellow'],
    'blue':    PALETTE['bright-blue'],
    'purple':  PALETTE['bright-purple'],
    'aqua':    PALETTE['bright-aqua'],
    'orange':  PALETTE['bright-orange'],
}


GB_LIGHT_BG0 = {
    'soft': PALETTE['light0-soft'],
    'hard': PALETTE['light0-hard']
}

LIGHT_COLORS = {
    'bg0':     GB_LIGHT_BG0.get(GRUVBOX_CONTRAST_LIGHT, PALETTE['light0']),
    'bg1':     PALETTE['light1'],
    'bg2':     PALETTE['light2'],
    'bg3':     PALETTE['light3'],
    'bg4':     PALETTE['light4'],

    'gray':    PALETTE['gray-244'],

    'fg0':     PALETTE['dark0'],
    'fg1':     PALETTE['dark1'],
    'fg2':     PALETTE['dark2'],
    'fg3':     PALETTE['dark3'],
    'fg4':     PALETTE['dark4'],

    'fg4-256': PALETTE['dark4-256'],

    'red':     PALETTE['faded-red'],
    'green':   PALETTE['faded-green'],
    'yellow':  PALETTE['faded-yellow'],
    'blue':    PALETTE['faded-blue'],
    'purple':  PALETTE['faded-purple'],
    'aqua':    PALETTE['faded-aqua'],
    'orange':  PALETTE['faded-orange'],
}


class GruvboxDarkStyle(Style):
    """
    The gruvbox style, dark.
    """

    styles = make_style(DARK_COLORS)
    background_color = DARK_COLORS['bg1']
    highlight_color = DARK_COLORS['bg2']
    line_number_color = DARK_COLORS['fg2']
    line_number_background_color = DARK_COLORS['bg0']


class GruvboxLightStyle(Style):
    """
    The gruvbox style, light.
    """

    styles = make_style(LIGHT_COLORS)
    background_color = LIGHT_COLORS['bg1']
    highlight_color = LIGHT_COLORS['bg2']
    line_number_color = LIGHT_COLORS['fg2']
    line_number_background_color = LIGHT_COLORS['bg0']
