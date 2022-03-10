"""this is for further usage"""
import os
from termcolor import colored


def highlight(text, word, color, case=False):
    """highlight single word in text, while full text is colored with color"""
    if case:
        print('[x] not implemented yet')
        return ''
    parts = text.split(word)
    selection = colored(word, color, None, ['reverse'])
    colored_parts = [colored(item, color) for item in parts]
    highlighted_text = selection.join(colored_parts)
    return highlighted_text
    
    
if __name__ == "__main__":
    os.system('color')
    text, word = 'this is word sentence with word to be colored', 'word'
    text, word = 'veryWordWithPartsWordsWorld.text', 'Word'
    
    highlighted_text = highlight(text, word, 'yellow', case=False)
    print(highlighted_text)
    