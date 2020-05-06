# virtual environment

# virtual env is a way that we can separate different python environment for different projects.
# why would we do something like this?
# lets say, we have multiple projects and they all rely on a single package lets say django.
# each one of these projects may using different version of django.
# now if we go and upgrade that package in our global site packages, then it could break couple of our websites.
# that might not what we want.
# it would be better if each of this projects have an isolated environment
# where they have only the dependencies and packages they need.
# thats what virtualenv allows us to do.
# it allows us to make those different python environments.
# lets go ahead and get started.

# first we need to install the virtual environment with pip.
"""pip install vitualenv"""

# now lets use virtualenv to make few different python environmment.
# first we like to make directory called Environments.
"""mkdir Environment"""
# now lets cd to that directory.
"""cd Environment"""
# if we do a dir here we can see that this dirctory is currently empty.
"""dir"""
# we can make our first virtual environment by
"""virtualenv pro1"""
# we can see this install setuptools and pip for us.
# now if we go into that environment, we can start installing packages.

# in order to activate this new python environment, we can-
"""pro1/Scripts/activate"""

# now it adds that to our promt.
# even we clear out our prompt, it says (pro1)
# we can also see that by-
"""where python"""
# we can do the same thing-
"""where pip"""

# we can see that the python and pip is both situated in prop1 and python soft file.
# now if we do a pip list here.
"""pip list"""
# now we can see here we only have pip,wheel and setuptools, not all the packages.
# lets go ahead and install few packages into this new environment.
"pip install numpy"

# now lets say we want to export this packages and version numbers to use it i another project.
# we can do that by-
"""pip freeze --local > REQUIRE.txt"""
# here what --local does?
# we can also our global site packages within virtual python env.
# we didnt choose to do that. but if we have than all thats global site packages available to us.
# if we use --local, then it will only takes the local dependencies that we have in our python virtual env.

# let us do a dir
"""dir"""
# now lets read the REQUIRE.txt.
"""type REQUIRE.txt"""

# now say that we want to get out of our python virtual environment.
# we want to get back to our global environment.
# all we have to do to get out our vertual environment is to type in-
"""deactivate"""
# now we can see our prompt no longer shows us (pro1)
# now if we type-
"""where python"""
"""where pip"""
"""pip list"""
# now we can see that we are using our global environment.
# if we do a dir here.
"""dir"""
# we still have pro1
# what if we want to get rid of that.
# first we have to deactivate it after that we have to delete the pro1 directory.
"""rmdir pro1 /S /Q"""

# now if we do a dir, then its gone.
"""dir"""

# now we still have this REQUIRE.txt file here.
# lets create another virtualenv.
# but this time we will specify the python version.
"""virtualenv -p /path/python2.6 pro2(py2)"""
# now if we do dir
"""dir"""
# we can see that we have pro2(py2)
# now lets activate that,
"""pro2(py2)/Scripts/activate"""
# now our prompt is changed. we see pro2(py2) 
# now lets see,
"""where python"""
"""python --version"""
# we can see that we are using python2.
# now if we want to install those pachages of REQUIRE.txt file we can-
"""pip install -r REQUIRE.txt"""
# now if we do a pip list
"""pip list"""
# we can see that we have all those packages installed.
# deactivate the environment.
"deactivate"

# virtual environments are meant to be for our dependencies and packages for our project.
# but they are not for our project files.
# we should not go to pro1 or pro2 and start work project file there.
# because we can delete the virtual environments anytime we want. then our project files will also be deleted by mistake.

