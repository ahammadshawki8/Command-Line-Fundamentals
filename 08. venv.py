# venv

# in this module, we will learn about built in standerd venv library to work with virtual environment.

# first lets cd to our environment file
"""f:"""
"""cd python\Environment"""

# we dont need to install anything. this package comes with the standerd library.
# before creating environment lets see our packages by pip list
"""pip list"""

# now lets create a new virtual environment.
"""python -m venv pro3"""
# when we use -m and create a virtual env like we did here,
# python will search our sys.path and execute that module as the main module.
# so this venv module expects the environment name as an arguement and then it will create a virtualenv for us.

# now we should have a new environmment. we can use dir method.
"""dir"""

# to activate this we can simply
"""pro3\Scripts\activate.bat"""

# now our environment is activated and we can see the environment name in brackets there.
# we can see the python and pip current path also.
"""where python"""
"""where pip"""

# the version of python that it will use in the environment is going to be same version when we create the environment.
# if we need to use a different version of python, then we need to use something like virtualenv instead.

# now lets us do a pip list again in this new environment.
"""pip list"""
# we can see that we have only pip and setuptools installed within this environment.
# now if we install some packages that will only installed in this new environment.
"""pip install pytz"""
"""pip install requests"""
# now lets run pip list again
"""pip list"""
# now we can see that it has installed all of those packages within our virtualenv.

# if we want to export the dependencies and packages as requirements.txt file, then we can use the pip freeze command.
"""pip freeze"""
"""pip freeze > requirements_3.txt"""

# to install the packages from requirements.txt file.
"""pip install -r requirements_3.txt"""

# now lets deactivate our environment.
"""deactivate"""
# now we can see that we no longer have the environment name in our prompt.

# if we want to delete the environment entirely from our machine, we can
"""rmdir pro3 /S /Q"""

# when we are working in a project and we want to make a virtual environment, then we can-
# 1. first make the project folder.
# 2. then make the environment inside the project folder naming that venv or virtual environment or something like that.
# 3. after that we can activate the virtualenv
# 4. install required packages with essential versions
# 5. create our project files in that project folder.
# 6. so these environment and project file remains separate and easy for us to work later.
# NOTE: it is common to put our virtualenv inside our project folder, but it is totally forbidden that to put project files in the virtualenv.
# because environment can be rebuild or change or ommit our project files which we dont want.

# another important thing is that we should commit our virtualenv to source control.
# if we ever look at a template getting more file than the python project, then they usually have virtual env ignored.
# it means they wont be able to commit it to source control.

# we should commit something like requirements.txt file so that people could enable to run our project intheir machine.
# but there is no need to add the environment itself.

# how to create environment with access to this system packages.
# if we do a pip list within pou system installation of python.
"""pip list"""
# there is a way that we can create a virtual env that have access to this packages.
# but this is less recommanded. anytime we need to use a package we should create a requirements.txt file and install the global packages again in our virtualenv.

# lets create that environment that have access to our global packages.
"""python -m venv access_pro --system-site-packages"""
# now we can activste this.
"""access_pro\Scripts\activate.bat"""
# we can see the environment name.
# if we do a pip list we can see that all of those system packages are also available inside of this virtualenv.
"""pip list"""
# now the additional packages that we install in this virtual environment still wont effect to the system environment.
"""pip install tenserflow"""

# but it is also possible to list those packages which we have installed only in this environment.
"""pip list --local"""

# if we deactivate the virtualenv and pip list to our global packages,
"""deactivate"""
"""pip list"""
# we can see that our tenserflow hadn't installed in this global packages.
# --local also works for pip freeze.
"""pip freeze --local"""
"""pip freeze --local > access_require.txt"""