#!/usr/bin/python3
"""Command interpreter entry point module."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def default(self, arg):
        """Catch commands if nothing else matches then."""
        self._precmd(arg)

    def _precmd(self, arg):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not match:
            return arg
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_val = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dictionary(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_val = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_val:
                attr_and_val = (match_attr_and_val.group(1) or "") + " " + (match_attr_and_val.group(2) or "")
        comm = method + " " + classname + " " + uid + " " + attr_and_val
        self.onecmd(comm)
        return comm

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
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            strng = arg.split(' ')
            if strng[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(strng) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(strng[0], strng[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        strng = arg.split(' ')
        if arg == "" or arg is None:
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
        """ Prints string repr. of instances based or not on the classname.
        """
        if arg != "":
            strng = arg.split(' ')
            if strng[0] not in storage.classes():
                print("** class doesn't exist **")
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
        match = re.search(rex, arg)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
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

    def do_count(self, arg):
        """Retrieves the instances of a class.
        """
        strng = arg.split(' ')
        if not strng[0]:
            print("** class name missing **")
        elif strng[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            match = [
                ky for ky in storage.all() if ky.startswith(
                    strng[0] + '.')]
            print(len(match))

    def update_dictionary(self, classname, uid, match_dict):
        """Method  to update an instance based on his ID with a dictionary
        """
        y = match_dict.replace("'", '"')
        t = json.loads(y)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attr, val in t.items():
                    if attr in attributes:
                        val = attributes[attr](val)
                    setattr(storage.all()[key], attr, val)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
