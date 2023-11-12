#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF"""
        print()
        return True


def do_create(self, arg):
    """Creates a new instance of BaseModel, saves it, and prints the id"""
    if not arg:
        print("** class name missing **")
        return
    try:
        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)
    except NameError:
        print("** class doesn't exist **")


def do_show(self, arg):
    """Prints the string representation of an instance"""
    args = arg.split()
    if not args or args[0] not in self.classes:
        print("** class name missing **" if not args else "** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = "{}.{}".format(args[0], args[1])
    print(self.classes[args[0]].__objects.get(key, "** no instance found **"))


def do_destroy(self, arg):
    """Deletes an instance based on the class name and id"""
    args = arg.split()
    if not args or args[0] not in self.classes:
        print("** class name missing **" if not args else "** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = "{}.{}".format(args[0], args[1])
    obj = self.classes[args[0]].__objects.get(key)
    if obj:
        del self.classes[args[0]].__objects[key]
        self.classes[args[0]].save()
    else:
        print("** no instance found **")


def do_all(self, arg):
    """Prints all string representation of all instances"""
    args = arg.split()
    if not args or args[0] not in self.classes:
        print(
            "** class doesn't exist **" if args else [str(obj) for obj in storage.all().values()])
        return
    print([str(obj) for obj in self.classes[args[0]].__objects.values()])


def do_update(self, arg):
    """Updates an instance based on the class name and id"""
    args = arg.split()
    if not args or args[0] not in self.classes:
        print("** class name missing **" if not args else "** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = "{}.{}".format(args[0], args[1])
    obj = self.classes[args[0]].__objects.get(key)
    if not obj:
        print("** no instance found **")
        return
    if len(args) < 3:
        print("** attribute name missing **")
        return
    if len(args) < 4:
        print("** value missing **")
        return
    setattr(obj, args[2], args[3])
    obj.save()
