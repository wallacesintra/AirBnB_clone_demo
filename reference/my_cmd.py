#!/usr/bin/env python3
import cmd
### This is a simple example of a command line interface using the cmd module


class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    prompt = "(hbnb)"
    def do_greet(self, line):
        if line:
            print("Hi, {}".format(line))
        else:
            print("Hi ")


   
    def do_add(self, line):
        """Add numbers together"""
        arr = line.split()
        sum = 0
        if len(arr) < 2:
            print("Usage: add <number1> <number2> ...")
            return
        else:
            try:
                for i in arr:
                    sum += int(i)
                print(sum)
            except ValueError:
                print("Usage: add <number1> <number2> ...")

    def do_EOF(self,line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
