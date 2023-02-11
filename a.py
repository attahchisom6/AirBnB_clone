#!/usr/bin/python3
"""Class to crate our command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """command line interpreter to handle classes and child classes"""

    prompt = "(hbnb) "

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

        if len(arg) < 2:
            print("** instance id missing **")

        else:
            all_obj = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key not in all_obj.keys():
                print("** no instance found **")
            else:
                print(all_obj[key])

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
        arg = line.split(" ")
        flag = 0

        if arg[0] is None or arg[0] == "":
            print("** class name missing **")
            return False

        try:
            classname = line.split(" ")[0]
            eval("{}()".format(classname))
        except IndexError:
            print("** class doesn't exist **")
            return False

        try:
            obj_idx = line.split(" ")[1]
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
            attr_name = line.split(" ")[2]
        except IndexError:
            print("** attribute name missing **")
            return False

        try:
            attr_value = line.split(" ")[3]
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
            except:
                setattr(class_change. attr_name, str(attr_value))
                storage.save()

    def help_update(self):
        """help message"""
        print("Enter update command to update and set class attributes")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
