# Intro with PowerShell

# we can use the cmd commands in powershell.
# but not only that we can also run many linux prompt command,
# and also some extra powerful features and functionality of powershell itself.
# such as:
    # powershell is a object based command line language.
    # the pipelines in powershell is way more powerful than cmd.
    # it is so fast for using thousands ofcmdlets (powershell commands)
    # it is not only compatible for windows but also other operating systems.
    # we can work with variables and perform math functions in powershell.

# first lets cd to our working directory.
"cd Documents\Pshell"
# see which files we have with dir.
"dir"
# we can also use the "ls" mathod of linux.
"ls"
# we can also use gci or Get-ChildItem
"gci"
"Get-ChildItem"
# lets take help about dir method.
"help dir"

# pipeline
# using two commands at once
# sort the directories
"dir | sort"
# sort the objects of the directory
"dir | sort-object"
# sort in descending
"dir | sort-object -Descending"
# we can sort by date(LastWriteTime)
"dir | sort-object -Property -LastWriteTime"
# we can use descending also for this date sorting.
"dir | sort-object -Property -LastWriteTime -Descending"

# we can use for loop also
"dir | foreach {2}"
# lets print the type of our objects and also the name of our object.
"""dir | foreach {"$($_.GetType().fullname)  -  $_.name"}"""
# so, dir giving foreach objects through pipeline and that is doing some operations for each object.

# powershell uses a very consistant naming of the commands
# it uses a verb-noun pair command naming for cmdlets.
# it means the command should be obious what we are trying to do.
# if we want to get the process then,
# the verb should be Get and noun should be Process.
# so the cmdlet would be Get-Process
"Get-Process"
# we can format them as list.
"Get-Process | format-list"
# or
"Get-Process | fl"
# we can also format them as table.
"Get-Process | format-table"
# or
"Get-Process | ft"
# we can select what we want to show
"dir | format-table name, Length, LastWriteTime"
# we cab see the service host that is currently processing by
"Get-Process -Name svchost"
# if we want to filter by id which are greater than 1000, then
"Get-Process -Name svchost | where id -gt 1000"
# we can use multiple filter by
"Get-Process -Name svchost | where {$_.id -gt 1000 -and $_.Handles -gt 500}"
# here $_ just refers to current object and we are filtering on our current object.
# if we want to copy that to our notepad then, we can use clip
"ps | clip"
# then open the notepad and ctrl+v
"notepad"

# if we want to get a list of services, then
"Get-Service"
# if we create a new object, then
"New-Object -Typename"

# we can see powershell version by
"$psversiontable"

# we can see the all modules available for powershell.
"Get-Module -listavailable"
# it gives us the modulenames and their version and compability.
# but right now it is hiding manny modules form us because of they are not compatible in our version.
# but we can make it to display all the modules that are available
"Get-Module -listavailable -skipeditioncheck" 
# we can see qhich modules we currently have
"Get-Module"
# we can see the command names of modules too
"Get-Command -module Microsoft.PowerShell.Management"
# we can see the unique nouns by
"Get-Command -module Microsoft.PowerShell.Management | Select-Object -Unique Noun"
# we can sort them by noun
"Get-Command -module Microsoft.PowerShell.Management | Select-Object -Unique Noun | Sort-Object Noun"
# we can import modules by
"Import-Module Microsoft.PowerShell.Management"
# for importing all the modules
"Get-Module | Import Module"
# check the module version
"Import-Module Microsoft.PowerShell.Management"
"(Get-Module Microsoft.PowerShell.Management).version"
# install modules
"Install-Module Microsoft.PowerShell.Management"
# update modules
"Update-Module Microsoft.PowerShell.Management"
# we can see all the commands that have certain parameter.
"Get-Command -ParameterName PassThru"

# we can use Get-Member to discover objects, properties and methods
"dir | Get-Member"

# we can launch command prompt in powershell
"cmd"
# now just exit form that cmd.
"exit()"

# using tab in powershell
# we can start typing and use tab and it will show us all possible optaions that we may use.
# if we run powershell in the ise it will give us intellisense.
# ise also have snippets
# we can go to edit-start snippets and it will give a list of all the snippest in powershell.
# we can launch the ise by
"ise"

# we can see the alias of different functions.
"Get-Alias dir"
# we can see all the alias too.
"Get-Alias"
# Geting help for a cmdlet
"Get-Help dir"
# we can update help
"Update-Help"
# we can also use the help command
"help dir"
# the difference between help and Get-Help is that
# Get-Help gives us all the information once at a time
# whereas help gives us the inforemation line by line.

# we can also use the -ShowWindow command after that
"help dir -ShowWindow"

# we can stop any service by
"Stop-Service servicename"
# it worked fine but we didn't see anything happen.
# there is a -PassThru command for many cmdlets those who dont print the output.
"Stop-Service BITS -PassThru"
# we can start a service by
"Start-Service BITS"
# but that may damage the system. instead of that we can
"(Get-Service BITS).start()"

# we can also initialize variable by
"$name = 'Shawki'"
# we can print that name by
"$name"
# we can print any strings by
"Hello world!"
# we dont need to use the echo command
# we can use some operations on our string variable
"$name + 'Boss'"
"$name += 'Boss'"

# we can also do math operations
"2+3"
"2-3"
"2*3"
"2/3" # etc
# we can even intialize variable and do the same operations
"$a = 2"
"$b = 3"
"$a + $b"

# we can stop our computer by
"Stop-Computer"
