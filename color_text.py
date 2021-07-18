
def red_text(text):
    return '\033[91;1m' + text + '\033[0m'

def green_text(text):
    return '\u001b[32;1m' + text + '\033[0m'

def blue_text(text):
    return "\u001b[34;1m" + text + '\033[0m'

def yellow_text(text):
    return "\u001b[33;1m"+ text + '\033[0m'

def magenta_text(text):
    return "\u001b[35;1m" + text + '\033[0m'

def cyan_text(text):
    return "\u001b[36;1m" + text + '\033[0m'

def white_text(text):
    return "\u001b[37;1m" + text + '\033[0m'



def red_background(text):
    return '\u001b[41;1m' + text + '\033[0m'

def green_background(text):
    return '\u001b[42;1m' + text + '\033[0m'

def blue_background(text):
    return "\u001b[44;1m" + text + '\033[0m'

def yellow_background(text):
    return "\u001b[43;1m"+ text + '\033[0m'

def magenta_background(text):
    return "\u001b[45;1m" + text + '\033[0m'

def cyan_background(text):
    return "\u001b[46;1m" + text + '\033[0m'

def white_background(text):
    return "\u001b[47;1m" + text + '\033[0m'


text = "hot mole IS HOT"
print(
    green_text(text),
    magenta_background(text),
    blue_background(red_text(text))
)
