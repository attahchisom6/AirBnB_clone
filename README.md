# AirBnB_clone


## Description
![](https://camo.githubusercontent.com/97788fc5310cea2961d9d8dbfa9cb4b6aacd420eb1efb27372af451d7f04b7a7/68747470733a2f2f692e696d6775722e636f6d2f6f764d4e79455a2e706e67)
## Purpose
 The purpose of the project include
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* UUID, `*args,` `**kwargs` and how to use it
* How to handle named arguments in a function

## Command interpreter
## Interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
## Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
