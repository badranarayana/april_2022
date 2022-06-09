"""
Virtual Environment in Python

"""
"""
A virtual environment is a tool that helps
to keep dependencies required by different projects separate
by creating isolated python virtual environments for them.
This is one of the most important tools that most of the Python developers use.

Why do we need a virtual environment?

Imagine a scenario where you are working on two web based python projects
 and one of them uses a Django 1.9
and the other uses Django 1.10 and so on.
In such situations virtual environment can be really useful
to maintain dependencies of both the projects.

When and where to use a virtual environment?

By default, every project on your system will use these same directories to store
and retrieve site packages (third party libraries).
How does this matter? Now, in the above example of two projects,
you have two versions of Django.
This is a real problem for Python since it can’t differentiate
between versions in the “site-packages” directory.
So both v1.9 and v1.10 would reside in the same directory with the same name.
This is where virtual environments come into play.
To solve this problem, we just need to create two separate virtual environments
for both the projects.
The great thing about this is that there are no limits to
the number of environments you can have since they’re just directories containing a few scripts.

How does a virtual environment work?

We use a module named virtualenv which is a tool to create isolated Python environments.
virtualenv creates a folder which contains all the necessary executables
to use the packages that a Python project would need.

Installing virtualenv

$ pip install virtualenv

Test your installation:

$ virtualenv --version

Using virtualenv
You can create a virtualenv using the following command:

$ virtualenv my_name


or
# create env with specific python version

$ virtualenv -p /usr/bin/python3 virtualenv_name

# activate env
$ source virtualenv_name/bin/activate

windows:
myenv\Scripts\activate


# pip is an tool to manage the python packages in your system

$ pip install <package_name> 

Or
$ pip install <package_name>==<version>


# uninstall python packages
$ pip uninstall <package_name>

"""