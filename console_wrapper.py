import os
import random
from termcolor import colored


class ConsoleWrapper():
    def __init__(self, prompt=None, prompt_color=None):
        if prompt is None:
            prompts = ['~< go >~# ', '>~ run ~<# ', '-{ do it }-# ', '**( foo )**# ']
            self.__prompt = random.choice(prompts)
        else:
            self.__prompt = prompt
            
        if prompt_color is None:
            self.__prompt_color = random.choice(['red', 'yellow', 'cyan'])
        else:
            self.__prompt_color = 'red'
            
        self.__last_command = ''
        self.__commands_history = []
        
    def _console_help(self):
        print(colored('console help:', 'cyan'))
        print(colored('    cls\clear            -clear console', 'cyan'))
        print(colored('    exit\quit            -exit from console', 'cyan'))
        print(colored('    last                 -last command', 'cyan'))
        print(colored('    history              -last command', 'cyan'))
        return None
        
    def run(self):
        """run console"""
        while True:
            try:
                query = input(colored(self.__prompt, self.__prompt_color, None, ['bold']))
                
            except KeyboardInterrupt:
                print()
                continue
                
            try:
                # clear query from white characters
                query = query.strip()
                if not query:
                    continue
                    
                # ********* execute command *********
                if query in ('exit', 'quit'):
                    return None
                    
                elif query in ('cls', 'clear'):
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')
                    continue
                    
                elif query == 'help':
                    self._console_help()
                    continue
                    
                elif query == 'last':
                    print(colored(self.__last_command, 'yellow'))
                    continue
                    
                elif query == 'history':
                    print(colored('\n'.join(self.__commands_history), 'yellow'))
                    continue
                    
                else:
                    pass
                    
                # ********* execute query *********
                # do something
                print(colored(self, 'magenta'))
                
            except KeyboardInterrupt:
                print()
                continue
                
            except Exception as err:
                print(colored('[!] unexpected error catched: {}'.format(err), 'magenta'))
                
            finally:
                if not query.strip():
                    continue
                self.__last_command = query
                self.__commands_history.append(query)
                
        return None
        
    def __str__(self):
        """print as show_db with matched_only and table_view"""
        return '<command executed>'
        
        
if __name__ == "__main__":
    if os.name == 'nt':
        os.system('color')
    console = ConsoleWrapper()
    console.run()
    