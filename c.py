#!/usr/bin/python3
"""Class to crate our command interpreter"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command line interpreter to handle classes and child classes"""

    prompt = "(hbnb) "

    command_list = [
            "create", "destroy", "show", "update", "all", "count"
            ]

    def precmd(self, arg):
        """this will provide another way to parse our command"""
        if "." in arg and "(" in arg and ")" in arg:
            arg_list = arg.split(".")
            classname = arg_list[0]
            other_list = arg_list[1].split("(")
            command = other_list[0]
            func_args_list = other_list[1].split(")")
            func_arg = func_args_list[0]
            if classname in storage.data_classes() and \
                    command in self.command_list:
                arg = "{} {} {}".format(command, classname, func_arg)
        return (arg)

    def do_EOF(self, line):
        """this will signal the end of the readline
        and hence loop out of the shell"""
        return (True)

    def help_EOF(self):
        """print EOF  help msg"""
        print("EOF command to exit the problem")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return (True)

    def help_quit(self):
        """help message"""
        print("Quit command to exit the program")

    def emptyline(self):
        """pressing the ENTER key wouldn't execute anything"""
        pass

    def do_create(self, classname):
        """this command will create a new instance of BaseModel"""
        if classname == "" or classname is None:
            print("** class name missing **")
        elif classname not in storage.data_classes():
            print("** class doesn't exist **")
            return (False)
        else:
            new_obj = storage.data_classes()[classname]()
            new_obj.save()
            print(new_obj.id)

    def help_create(self):
        """help message"""
        print("Enter create command to cerate an instance")

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""
        arg = line.split(" ")
        if arg[0] == "" or arg[0] is None:
            print("** class name missing **")
            return False
        elif not arg[0] in storage.data_classes():
            print("** class doesn't exist **")

        elif len(arg) < 2:
            print("** instance id missing **")

        else:
            all_obj = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in all_obj.keys():
                print("** no instance found **")
            else:
                print(all_obj[key])
                return False

    def help_show(self):
        """help message"""
        print("Enter show command to display instances \
                in string format")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        save the change into the JSON file"""
        arg = line.split(" ")
        if arg[0] == "" or arg[0] is None:
            print("** class name missing **")
        elif not arg[0] in storage.data_classes():
            print("** class doesn't exist **")
            return (False)

        elif len(arg) < 2:
            print("** instance id missing **")
            return (False)

        else:
            all_obj = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in all_obj.keys():
                print("** no instance found **")
            else:
                del all_obj[key]
                storage.save()

    def help_destroy(self):
        """help message"""
        print("Enter destroy command to delete an instance")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        if line != "":
            arg = line.split(" ")
            if not arg[0] in storage.data_classes():
                print("** class doesn't exist **")
            else:
                str_obj = [
                        str(obj) for key, obj in storage.all().items()
                        if obj.__class__.__name__ == arg[0]
                        ]
                print(str_obj)
        else:
            str_obj = [str(obj) for key, obj in storage.all()]
            print(str_obj)

    def help_all(self):
        """help message"""
        print("Enter all command to display all instances \
                in string format")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        strr = ""
        for args in line.split(","):
            strr = strr +  args

        arg = shlex.split(strr)
        if arg[0] is None or arg[0] == "":
            print("** class name missing **")
            return False

        try:
            classname = arg[0]
            eval("{}()".format(classname))
        except KeyError:
            print("** class doesn't exist **")
            return False

        try:
            obj_idx = arg[1]
        except IndexError:
            print("** instance id missing **")
            return False

        all_obj = storage.all()
        try:
            class_change = all_obj["{}.{}".format(classname, obj_idx)]
        except IndexError:
            print("** no instance found **")
            return False

        try:
            attr_name = arg[2]
        except IndexError:
            print("** attribute name missing **")
            return False

        try:
            attr_value = arg[3]
        except IndexError:
            print("** value missing **")
            return False

        if attr_value.isdecimal() is True:
            setattr(class_change, attr_name, int(attr_value))
            storage.save()
        else:
            try:
                setattr(class_change, attr_name, float(attr_value))
                storage.save()
            except Exception:
                setattr(class_change, attr_name, str(attr_value))
                storage.save()

    def help_update(self):
        """help message"""
        print("Enter update command to update and set class attributes")

    def do_count(self, arg):
        """this command method will count the number of instances a class
        at a particular time
        """
        count = 0
        all_obj = storage.all()
        for key in all_obj.keys():
            key_class = key.split(".")[0]
            if key_class == arg:
                count = count + 1
        print(count)

    def help_count(self):
        """help mwssage"""
        print("Enter the count command to get the number of instances \
                in the class")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
