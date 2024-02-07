#!/usr/bin/python3
"""Command interpreter entry point module."""

import cmd
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Module to exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """Module to handle End of File character
        """
        print()
        return True
    
    def emptyline(self):
        """Module to do nothing when ENTER is pressed.
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and save it to JSON.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            a = storage.classes()[arg]()
            a.save()
            print(a.id)
        
    def do_show(self, arg):
        """Prints the string representation of an instance 
        based on the class name and id.
        """
        strng = arg.split(' ')
        if strng == "" or strng is None:
            print("** class name missing **")
        elif strng[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(strng) < 2:
            key = strng[0] + "." + strng[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id 
        (save the change into the JSON file).
        """
        strng = arg.split(' ')
        if strng == "" or strng is None:
            print("** class name missing **")
        elif strng[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(strng) < 2:
            print("** instance id missing **")    
        else:
            key = strng[0] + "." + strng[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
    
    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name.
        """
        if arg != "":
            strng = arg.split(' ')
            if strng[0] not in storage.classes():
                print("** class doesn't exitst **")
            else:
                lst = [str(obj) for key, obj in storage.all().items()
                if type(obj).__name__ == strng[0]]
                print(lst)
        else:
            n_lst = [str(obj) for key, obj in storage.all().items()]
            print(n_lst)
    
    def do_update(self, arg):
        """Updates an instance by adding or updating attribute.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        tally = re.search(rex, arg)
        classname = tally.group(1)
        uid = tally.group(2)
        attribute = tally.group(3)
        value = tally.group(4)
        if not tally:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                num = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        num = float
                    else:
                        num = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif num:
                    try:
                        value = num(value)
                    except ValueError:
                        pass  
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
