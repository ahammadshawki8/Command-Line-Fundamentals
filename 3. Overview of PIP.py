# module 41
# python pip

# pip is the python package manager.
# here all the code we will do in the terminal.

# to see all the resources and commands that we can use in pip, we can write.
"""pip help"""
# we can see there a lot of commands and general options.

# we can see the commands.
#  Usage:
#   pip <command> [options]

# Commands:
#   install                     Install packages.
#   download                    Download packages.
#   uninstall                   Uninstall packages.
#   freeze                      Output installed packages in requirements format.      
#   list                        List installed packages.
#   show                        Show information about installed packages.
#   check                       Verify installed packages have compatible dependencies.
#   config                      Manage local and global configuration.
#   search                      Search PyPI for packages.
#   wheel                       Build wheels from your requirements.
#   hash                        Compute hashes of package archives.
#   completion                  A helper command used for command completion.
#   debug                       Show information useful for debugging.
#   help                        Show help for commands.

# we can see all the general options
# General Options:
#   -h, --help                  Show help.
#   --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
#   -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
#   -V, --version               Show version and exit.
#   -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging        
#                               levels).
#   --log <path>                Path to a verbose appending log.
#   --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
#   --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
#   --timeout <sec>             Set the socket timeout (default 15 seconds).
#   --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
#   --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
#   --cert <path>               Path to alternate CA bundle.
#   --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
#   --cache-dir <dir>           Store the cache data in <dir>.
#   --no-cache-dir              Disable the cache.
#   --disable-pip-version-check
#                               Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.       
#   --no-color                  Suppress colored output
#   --no-python-version-warning
#                               Silence deprecation warnings for upcoming unsupported Pythons.


# we can also add the command name after help command ton get the help for a specific command.
"""pip help install"""
# now we can see it prints out a lot of commands and options for install command.

# find a package what it do.
# lets say we know the name of a package, but dont know what it do?
# then we can use pip search command.
"""pip search scikit learn"""
# it will also give us another packages which is simmilar to the name of scikit learn.

# once we got the pachage name we can install it with install command.
"""pip install scikit-learn"""

# if we want to look at our installed packages then we can use list command.
"""pip list"""
# we can see the list name and the version number.

# if we dont want that package then we can use uninstall command.
"""pip uninstall scikit-learn"""

# when we have listed our packages we saw their version numbers too.
# how do we know that this version is the latest version of that package?
# we can do that by adding a option(--outdated or -o) after list command.
"""pip list --outdated"""
"""pip list -o"""

# to update any package we can use the -U option between install command and package name.
"""pip install -U setuptools"""

# lets say we are working on a project, and we want to provide someone else with a list of the packages they need for that project.
# one thing we can do is that type down pip list and they will manually copy down the project name.
# if we have a really long list of packages, then it is definately not the best way of doing that.
# for this we are going to use freeze command.
"""pip freeze"""
# what is does is it put all of the packages and version number in our required format.
# if we want to send this to anybody then we can create a .txt file by adding the file name with > sign after freeze command.
"""pip freeze > requirements.txt"""

# now to see the requirements.txt file we can use the cat command.
"""cat requirements.txt"""

# now if we send this file to anybody, how they would be able to install this packages with this file.
# here we need to add -r option after install command.
# -r means we are using a requirement file.
# after -r option, we need to add the file name.
"""pip install -r requirements.txt"""

# these are the simple basics that we are going to use pip for most of the time.
# lets see a simple trick.
# if we see the outdated packages.
"""pip list --outdated"""
# we can see that there is multiple packages which are outdated.
# pip doesnt have any command to upgrade all of the outdated packages at a time.
# so we can upgrade them manually using -U option.
# but if we have a lot of packages then that would be a lot of time.

# but we have a command line which can do this for us.
#"""pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U"""
# for the older version of pip, we can do this instead.
#"""pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U"""

# lets go what this means.
# first we have pip freeze which output all of the packages that we have currently here.
# --local means if we are in a virtual environment, that has access to our global packages, then it will only print out local packages.
# and then we pipe that output to the grep command here. The grep is to skip editable ("-e") package definitions
# after that it runs grep command it get piped in this cut command.
# the cut command set this delimiter to a eual sign then it only returns the first arguement back of that result.
# so the cut command will cut out after or before the delimeter.
# the last par of the command takes this output as arguements one at a time and install the upgraded version of the packages.

# this actually works for linux and mac.
# for windows we can use this command-
""" pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}"""
# this will basically check all the packages and upgrade the outdated ones. it just skip the upgraged ones.
 
# lets see what it does step by step.
# first we have pip freeze which output all of the packages that we have currently here.
# then we have a line full of commands this this just setting the deimeter 
# and returning the previous part of the delimeter i mean the package name without their version number.
# last command take the packages one by one and upgrade it if they are not updated.


# now if we see for the outdated packages, we can see that there is not package listed.
"""pip list -o"""