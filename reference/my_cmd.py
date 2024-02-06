#!/usr/bin/env python3
import cmd
# from cmd import Cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    def do_greet(self, line):
        print("Hello")

    def do_greetName(self, line):
        if line:
            print("Hi {}".format(line))
        else:
            print("Hi ")

    def do_EOF(self,line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
