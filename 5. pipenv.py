# Pipenv

# pipenv is a new way to us combining package management with virtual environment.
# and it is also a highly recommanded packaging tool for python.org
# a lot of teams and companies are switching over from pip to pipenv.
# sp it is definately a nice tool for learn.
# basically it is combining the features of pip and virtualenv.

# first lets go over pip and virtualenv.

# pip is a way for us to install additional packages that allows us to add tons of functionality that doesn't exits in python standerd libary.
# for example, if we want to do the image manipulation, then python might not have the best toolsbox.
# but we can use pip to install pillow library and work with the image manipulation.

# a virtualenv is a way for us to have a specific environment for each project or application that we are building.
# for example, we can have one application that runs with python 2.7 and django 1.5.
# and then another project that runs with python 3.8 and django 1.9
# so each of the projects have their own python and own packages.
# some people just ignore virtualenv and do their work in the global packages.
# but we should not do it because if we update those pachages or update python, then our project may be crash.
# so it is recommanded to split those projects using virtual environment.

# without pipenv, we handle the package management with pip and virtual environment management with virtualenv.
# but now with pipenv, these can be handled by one tool that simplifies the process.

# first we need to install pipenv using pip
"""pip install pipenv"""

# once we have installed lets pretend that we are starting a new project.
# now we can see how to install packages for that project and also create virtualenv automatically.

# first lets cd to our location where we want to create or project.
"cd Environment/pro2" 
# right now this is an empty directory. we can see that by dir
"dir"
# if we re using the old method, then in this point we will creating a virtualenv. 
# and then we need to manually activate the environment and then we need to start installing our essential packages.
# but with pipenv this is built_in together now.
# so, instead of creating a virtualenv manually we simply going to install the pachages that we want with pipenv.
# lets say we want to use the requests package for the project.
"""pipenv install requests"""
# lets look what pipenv do for us.
# first it see if wehave a virtualenv for this project or not.
# if not then it will create a virtualenv for us.
# then it gives us a location of Pipfile.
# then it says that it is using which version of python.
# then it actually goes through and creates the virtualenv for us and gives us the location of our virtualenv.
# this virtualenv is actually like a regular virtualenv that we used in past.
# so we can navigate the location and activate it manually if we like, 
# but pipenv gives us simpler command to interect with the environment than to activate it manually.
# the it creates a Pipfile.
# A pip file is a file that describes our environment and how we can build it again from scratch.
# this is simmilar with requirements.txt file that we used before with pip freeze command.
# and it is actually a replace for the requirements.txt file within pipenv.
# after creating the pipfile, then it actually installs our requests package.
# then it added requests package to our pip file packages.
# then it says that it doesn't found pipfile.lock so it is creating that.
# pipfile.lock is another file got creted and it is simmilar to the pipfile but some key differences.
# basically pipfile.lock is a file that not supposed to touch. it is a file that gets generated and produce the termanistis build.
# lastly it tells us, that we can activate the virtualenv simply by saying "pipenv shell".
# and if we want to run a command inside that vartualenv then we can do "pipenv run"

# before we activate the virtualenv, lets look at the pipfile and pipfile.lock.
# lets open them in our visual studio code.

# first lets look at the pipfile
# it is pretty simple.
# the format it is using is called TOML
# TOML is designed to be a minimal format that mostly contains the keys and values within the sections.
# we have a source section here. it shows the url of where we are downloading the python packages from.
# then we have a packages section. there we can see we currently have requests package.
# and it says requests = "*". it means we didnt specify the version of requests package when we install it.
# if we had specify the version name before, then the package witll be equal to that.
# if we change the version name of requests package inside the pipfile, then another time if we update or install it it will install the specific version.
# lastly, we have the requires section. here it just shows the python_version.
# we could change that if we like.
# note: pipfile is editable. we can add packages here and rerun the install command.
# then it will install the new packages.

# now lets look at the pipfile.lock
# we can see that this one is bit more complicated.
# this is a file that we are not allowed to meant to change manually.
# this is a generated file which has more details information about our current environment.
# if we scrool down here we can see that we have some hashes and we have more packages than requests.
# this file even contains the dependencies that are installed when we  installed the request package.
# not only that but also it has the exact version of each of the packages that we installed.
# so this is the good thing about having this pipfile.lock.
# this will give us a termenestic build. it means these lock file will absolutely give us the exact same environment everytime.
# we can only get a different build if we explicitely update the lock file.

# so we have a problem before that updating package can hamper our project.
# pipfile can see a new version of package and update them accordingly.
# and when we are sure that all of our code is still working after we update those packages.
# then we can simply update the lock file which will give us the exact packages that was installed at the time that we know work well.
# and once we update the pipfile.lock file, then we can push that all to production.

# now lets activate our environment and see some other commands.
# to activate our environment we can simply-
"""pipenv shell"""
# now we can see that our environment is activated.
# we can see that we have (pro2) before the command line.
# we can see the python interpreter location.
"""where python"""
# or we can import sys.
"""python"""
""">>> import sys"""
""">>> sys.executable"""
# executable attribute will give us the current interpreter location.
# so whatever we installed in this project will be separate from our other project on our machine.
# since we have request in the environment then we can import that as well.
""">>> import requests"""
# now lets exit out of python.
""">>> exit()"""

# to deactivate our environment we can see exit command.
"""exit"""
# note here we should not use the deactivate command.
# because when we activate pipenv it creates a subshell.
# if we use deactivate command, then it wont exit teh shells properly.

# we can actually run commands within our virtual environment without actually activating them.
# we can do that by pipenv run command.
"""pipenv run python"""
""">>> import sys"""
""">>> sys.executable"""
""">>> requests"""
""">>> exit()"""
# we can see that this python is running within our environment.
# we can write script that way as well.

# now lets install more pachages for this project.
# we could do them one at a time by using the install command.
# but we can also install several packages from a existing project.
# we can use the requirements.txt file.
"""pipenv install -r REQUIRE.txt"""
# we have to enter the path of our requirements.txt file after -r option.
# now lets open our pipfile.
# we can see that in our packages system new packages are added to our pipfile
# and those are uthe exact packages version that we listed in our requirements.txt file.
# in pip we create requirements.txt file by pip freeze.
# in pipenv we can do that by-
"""pipenv lock -r"""
# this displays the way that our file will be displayed in a requirements.txt file. 

# now lets see how to install packages only in a dev environment.
# there might be some packages that we onlly need in the dev environment but dont need in the production.
# for example, we need pytest to test our code. but we dont need that to ship our code to production.
# to do these we can simply install a package like normal and install the --dev option at the end.
"""pipen install pytest --dev"""
# now we can see that it says addinf pytest to Pipfile's [dev-packages]...
# if we open our pipfile we can see that it didnt add anything to our packages section.
# instead of that it creates a new section called dev-packages and it added pytest to that.
# so it knows how to keep those separate so this is a nice feature of pipenv.

# uninstall a package
"""pipenv uninstall requests"""
# if we go to our pip file. we can see that we no longer have requests package.

# lets make change in the pipfile manually.
# lets say we want to use a different version of python for this environment.
# if we are using the old way of virtualenv, 
# then we might need to export our requirements.txt file and manipulate it.
# and then delete the virtual environment and recreate it from scratch.
# but using pipenv is going to be a lot easier. there are couple of ways that we can do this.
# first method is, we can just come in here into our pipfile and change the python version.
# now we need to recreate our virtual environment.
# to do this we can simply tell pipenv that our environment should be recreated.
"""pipenv --python 3.6"""
# now if we run python
"""pipenv run python"""
# we can see that we are using a new version of python.
# and we are still using the virtualenv
""">>> import sys"""
""">>> sys.executable"""
""">>> exit()"""

# another way we could done that is to remove the environment completely
# and then recreate that from scratch using the pipfile.
# if our environment become very crowded, then we should remove the environment completely.

# first we need to open pipfile and change python version.
# now lets open our terminal and remove the vertualenv completely.
"""pipenv --rm"""
# now our pipfile still exits with all the packages information.
# now lets create a new virtual environment.
"""pipenv install""" # we dont need to put anything here.
# it will create a new virtualenv with all our changes.

# to see the path of the virtual environment.
"""pipenv --venv"""
# so we can goto that path and use the activate and deactivate command manually if we want.

# one nice feature of pipenv is that we can easily check for non-security vaulnabities for any of our installed packages.
# to do that we can simply say
"""pipenv check"""
# we can see it gives us some issues and feedbacks here.
# so it is really nice to have the feedbacks to make our project better.

# now lets change the version of any of our packages.
# now lets run install command again to install those changes.
"""pipenv install"""

# another feature of pipenv is pipenv graph.
# that will display a dependecies graph showing our packages and dependencies for each of those.
"""pipenv graph"""
# here we can see that what package is depends on what package.

# now lets see what we should do when we are ready to push our code to production.
# currently we are using pipfile to install our packages.
# but pipfile isn't terminastic. but pipfile.lock is terminastic.
# it means pipfile.lock has the exact hashes and versions for specific packages that we are currently using in our project.
# whereas the pipfile might just tell us to grab the lastest version of the package.
# now getting the latest version is fine in development but when we push our code to production, we want to know what exact version of packages that have already passed our testing.
# once we have tested all our code and we are ready to push them to production,
# then we can creat and update the pipfile.lock with the current dependencies by saying.
"""pipenv lock"""
# we can see that it says that it updated that pipfile.lock.
# once that done then we can take our pipfile.lock and move that to our production environment.
# and once we are ready to install everything that in our pipfile.lock
# then we can simply run the command
"""pipenv install --ignore-pipfile"""
# that will create a environment what is in pipfile.lock and ignore the pipfile that ususally used by default.

# setting environment variables that are specific to environment.
# this is extreamly important.
# for example, if we are working on multiple flask and django project 
# and want to have environment variables for each project that contain the project secret key and datbase connection and things like that.
# then it will nice to have virtual environment handle this without needing to do that manually.
# the way we can do it in pipenv is to create a .env file within our project directory.
# and we can set multiple environment variables within that file.

# so lets us create a file in pro3 nemed (.env)
# now lets add environment variables to this .env file
# SECRET_KEY=mysecretkey
# DB_PASS=passwordsecreted

# now lets go back to the command prompt and run python within our environment.
"""pipenv run python"""
""">>> import os"""
""">>> os.environ.get("SECRET_KEY")"""
"""output: 'mysecretkey'"""

# so we can see that pipenv is very nice and powerful tool.
# we should use it for different project instead of pip and virtualenv.
