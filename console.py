#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """Simple command interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit the program"""
        return True

    def do_create(self, line):
        """Create an instance"""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Show an instance"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
            elif args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Destroy an instance"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) < 2:
                print("** instance id missing **")
            elif args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Show all instances"""
        if line and line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances = [str(obj) for obj in storage.all().values()
                         if not line or type(obj).__name__ == line]
            print(instances)

    def do_count(self, line):
        """Count instances of a class"""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            count = sum(1 for k in storage.all() if k.startswith(line + '.'))
            print(count)

    def do_update(self, line):
        """Update an instance"""
        args = line.split()
        if not line or len(args) < 3:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instance = storage.all()[key]
            setattr(instance, args[2], args[3])
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
