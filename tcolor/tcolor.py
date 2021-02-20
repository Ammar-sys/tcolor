class colors:
    highlight_dict = {
        'gray': '\x1b[7m',
        'pink': '\x1b[45m',
        'black': '\x1b[40m',
        'yellow': '\x1b[43m',
        'green': '\x1b[42m',
        'blue': '\x1b[44m',
        'red': '\x1b[41m'
    }

    color_dict = {
        'pink': '\033[95m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'black': '\x1b[30m',
        'orange': '\033[38;2;255;69;0m'
    }

    text_markup_dict = {
        'bold': '\033[1m',
        'underline': '\033[4m',
        'italic': '\x1B[3m',
        'striked': ''
    }

clr = ['\033[91m', '\033[38;2;255;69;0m', '\033[93m', '\033[92m', '\033[94m']
end = '\033[0m'
def prainbow(text: str):
    import secrets
    return ''.join([secrets.choice(clr) + i for i in text]) + end


def pcolor(text: str, color: str, markup: list = None, highlight: str = None):
    try:
        expression = colors.color_dict[color] + text + end
        if markup is None:
            if highlight is None:
                return f'{expression}'
            else:
                return colors.highlight_dict[highlight] + expression

        if markup is not None:
            expression_markup = "".join([colors.text_markup_dict[i] for i in markup]) + colors.color_dict[color] + text + end
            if 'striked' not in markup:
                if highlight is None:
                    return f'{expression_markup}'
                else:
                    return colors.highlight_dict[highlight] + expression_markup
            else:
                no_color = text.split(expression_markup)
                no_text = expression_markup.split(text)
                striked_no_color = "".join([u'\u0336{}'.format(i) for i in no_color[0]]) + '\u0336'
                return colors.highlight_dict[highlight] + no_text[0] + striked_no_color + no_text[1]

    except KeyError:
        raise KeyError('You\'re proving a invalid argument, please look at the acceptable options at '
                       'https://www.github.com/ammar-sys/colors')


def prgb(text: str, rgb: list, markup: list = None, highlight: str = None):
    try:
        if any(i > 255 or i < 0 for i in rgb):
            raise KeyError
        expression = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}" + end
        if markup is None:
            if highlight is None:
                return expression
            else:
                return colors.highlight_dict[highlight] + expression
        if markup is not None:
            expression_markup = " ".join([colors.text_markup_dict[i] for i in markup]) + expression
            if 'striked' not in markup:
                if highlight is None:
                    return expression_markup
                else:
                    return colors.highlight_dict[highlight] + expression_markup
            else:
                no_color = text.split(expression_markup)
                no_text = expression_markup.split(text)
                striked_no_color = "".join([u'\u0336{}'.format(i) for i in no_color[0]]) + '\u0336'
                if highlight is None:
                    return no_text[0] + striked_no_color + no_text[1]
                else:
                    return colors.highlight_dict[highlight] + no_text[0] + striked_no_color + no_text[1]

    except KeyError:
        raise KeyError('You\'re proving a invalid argument, please look at the acceptable options at '
                       'https://www.github.com/ammar-sys/colors')

printcolor, printrgb = pcolor, prgb
