# TColor

![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

This is a simple package to print colored messages using ASCI to the terminal built with python 3.

# Usage of TColor

To install this package use, 
```
pip install tcolor
```

Usage of it is pretty straight-forward,
```py
from tcolor import prgb, pcolor, prainbow

print(prainbow('Hello'))
print(prgb('World', rgb=[255, 0, 0]))
print(pcolor('!', 'black'))
```

TColor has 3 main functions, 
- prainbow 
- prgb 
- pcolor

**prainbow** takes a single parameter which is text to return as rainbow

**prgb** takes 2 mandatory & 2 optional parameters. text (str), rgb (list) being mandatory and markup (list) & highlight 
(str) being optional. 
- text ; text to return
- rgb ; color of the text \[R, G, B]
- markup ; what markups to use on the text (see bellow)
- highlight ; color to highlight the text with

**pcolor** being same as prgb but instead of a rgb parameter it takes a color in form of a string (see bellow for accepted ones)

# List of accepted values

    highlight_values = [
        'gray',
        'pink',
        'black',
        'yellow',
        'green',
        'blue',
        'red'
    ]

    color_values = [
        'pink',
        'blue',
        'cyan',
        'green',
        'yellow',
        'red',
        'black',
        'orange'
    ]

    text_markup_values = [
        'bold',
        'underline',
        'italic',
        'striked'
    ]

**RGB** parameter takes any values from 0 to 255.
