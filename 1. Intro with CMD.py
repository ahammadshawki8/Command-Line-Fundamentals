# in this module we are going to learn how to use command prompt in windows.
# it is essential for all of windows users especially for developers.

# note that: here casing doesn't matter.

# system info
# we can see all the information of our system using
"SYSTEMINFO"

# we can change the color too.
"COLOR /?"
# colors
    # 1 = Blue        9 = Light Blue
    # 2 = Green       A = Light Green
    # 3 = Aqua        B = Light Aqua
    # 4 = Red         C = Light Red
    # 5 = Purple      D = Light Purple
    # 6 = Yellow      E = Light Yellow
    # 7 = White       F = Bright White

# so we can change the color by this format.
#color BackgroundForground
"COLOR 04"
# if we write the color again
"COLOR"
# it will set to default color.
# if we set one color then it will be set to the forground color.

# it wont set the color permanently. to set the color permanently we have to do it from properties.

# to clear the screen we can use cls(clear screen) command.
"cls"

# we can also right click the title bar and go to properties.
# here we have lots of options.
# we can change cursor size, buffer size, edit options, text selections.
# in fonts we can change font, size and pixels.
# in layout we can change the screen buffer size, windows size and position.
# in color, we can change the colors.
# in terminal, we havaae terminal colors, cursor shape, cursor colors and terminal scrolling.

# to see and change the date we can use date command.
"DATE"
# if we dont want to change the date then we can press enter.

# to see the time, we can use the time command.
"TIME"

# now we will see change directory command.
# to go back from one folder, we will write
"cd .."
# and if we want re-enter the folder, we can write the folder name or location after cd command.
"cd User"
# if we want to change the drive then we can write the drive name and write a colon after them.
"f:"

# dir COMMAND
# it will show us all the directories of our folder
"dir"
# dirrectory command has also many sun-commands.
# to see then we can,
"dir /?"

# we can see that we have lots of commands.

# Displays a list of files and subdirectories in a directory.

# DIR [drive:][path][filename] [/A[[:]attributes]] [/B] [/C] [/D] [/L] [/N]
#   [/O[[:]sortorder]] [/P] [/Q] [/R] [/S] [/T[[:]timefield]] [/W] [/X] [/4]

#   [drive:][path][filename]
#               Specifies drive, directory, and/or files to list.

#   /A          Displays files with specified attributes.
#   attributes   D  Directories                R  Read-only files
#                H  Hidden files               A  Files ready for archiving
#                S  System files               I  Not content indexed files
#                L  Reparse Points             O  Offline files
#                -  Prefix meaning not
#   /B          Uses bare format (no heading information or summary).
#   /C          Display the thousand separator in file sizes.  This is the
#               default.  Use /-C to disable display of separator.
#   /D          Same as wide but files are list sorted by column.
#   /L          Uses lowercase.
#   /N          New long list format where filenames are on the far right.
#   /O          List by files in sorted order.
#   sortorder    N  By name (alphabetic)       S  By size (smallest first)
#                E  By extension (alphabetic)  D  By date/time (oldest first)
#                G  Group directories first    -  Prefix to reverse order
#   /P          Pauses after each screenful of information.
#   /Q          Display the owner of the file.
#   /R          Display alternate data streams of the file.
#   /S          Displays files in specified directory and all subdirectories.
#   /T          Controls which time field displayed or used for sorting
#   timefield   C  Creation
#               A  Last Access
#               W  Last Written
#   /W          Uses wide list format.
#   /X          This displays the short names generated for non-8dot3 file
#               names.  The format is that of /N with the short name inserted
#               before the long name. If no short name is present, blanks are
#               displayed in its place.
#   /4          Displays four-digit years

# Switches may be preset in the DIRCMD environment variable.  Override
# preset switches by prefixing any switch with - (hyphen)--for example, /-W.


# if we want to see only directories
"dir /AD"
# if we want to see the files not with dates and extra. we can,
"dir /B"
# B means base mood.
# even we can mix two commands also.
"dir /AD /B"
# we can sort the files by /O sub-command.
# to order by name we need to use N after that.
"dir /ON"
# it prints all the files in alphabetical order.
# if we want to print then in descending order, then we can use a hiphen(-) between O and N
"dir /O-N"
# if we want to see that in the base mode then we can add /B between dir and /O
"dir /B /O-N"
# we can also sort by date by adding D after /O
"dir /OD"
# we can see that the latest folder prints last.
# we can reverse the sort using hiphen(-)
"dir /O-D"

# to print the previous command what we did, we can use the upper arrow key.
# to print the next command what we did, we can use the lower arrow key.

# to see all nested folders, we can write /S command
"dir /S"

# we can use this with /P command too.
# P means page. it will print the result like pages.
"dir /S /P"

# Wild cards
# we have two wild cards * and ?

# if we want to see the files name which start with a
"dir a*"
# if we want to see only the base mood.
"dir /B a*"
# if we want to see the file name start with am
"dir /B am*"
# what if we write only star(*)? it will give us all files.
# * means give us all files.
"dir /B *"
# if we want to see the files with certain extension, we can write the extention name with dot(.) after *
"dir /B *.zip"

# if we use question mark(?) it will tell us the files name which have single lettered name.
"dir /B ?"
# if we want to see the files name which have less than or equal to seven lettered name, then we can add more question marks.
"dir /B ???????"
# if we can also print them with extension.
"dir /B ???????.zip"

# so we can specify what the number or our file name with ?
# if we use .* after ? mark, then it will print all files which have certain numbered name.
"dir /B ????????.*"
# we can also use the ? mark in extensions too.
"dir /B ??????.?????"
# we can also mix the letter and ? mark too.
"dir /B am?????.*" 
# we can also use this with *.
"dir /B am*.*"

# RD/RMDIR COMMAND
# rmdir means remove directory.
# lets see the subcommands of rmdir.
"rmdir /?"
# Removes (deletes) a directory.

# RMDIR [/S] [/Q] [drive:]path
# RD [/S] [/Q] [drive:]path

#     /S      Removes all directories and files in the specified directory
#             in addition to the directory itself.  Used to remove a directory
#             tree.

#     /Q      Quiet mode, do not ask if ok to remove a directory tree with /S


# lets say we want to delete compressed directory.
"rmdir compressed"
# we cant re-back the files from recycle bin.
"rmdir documents /S /Q"
# /S delets all the sun directories.
# /Q is quite mode. it deletes all the directories quitely.

# MKDIR / MD COMMAND
# mkdir means make directory.
# lets see the subcommands first.
"mkdir /?"

# Creates a directory.

# MKDIR [drive:]path
# MD [drive:]path

# If Command Extensions are enabled MKDIR changes as follows:

# MKDIR creates any intermediate directories in the path, if needed.
# For example, assume \a does not exist then:

#     mkdir \a\b\c\d

# is the same as:

#     mkdir \a
#     chdir \a
#     mkdir b
#     chdir b
#     mkdir c
#     chdir c
#     mkdir d

# which is what you would have to type if extensions were disabled.

# lets make one directory.
"mkdir prac"
# if we want to make multiple directories such as dir1 and dir2.
"mkdir dir1 dir2"
# if we want to make single directory with space then we have to use double quotes("")
'mkdir "single dirctory"'
# now lets delete all the new directories
'rmdir prac dir1 dir2'
# if we want to make directory in the single directory which we have made earliar.
# we can enter the single dirctory with cd and create new directory with mkdir.
'cd "single directory"'
'mkdir new1'
# but we can do it at once.
'mkdir "single directory"/new1'
# we can use both the slash and the back slash.
# but back-slash is recommanded for this type of location. because slash is used for sub command.
# we can make directory in diffrenrent folders at once.
'mkdir "single directory"/new1 bye/hi'

# ECHO COMMAND
# echo command is use for making files.
"echo hey I am a coder > coder.txt"
# here we have to write the contents of the file, then we have to use the > sign,
# after that we will write the file name with extension.
# we can see the file manually
# but we wont do that. we will see the file in terminal.
# we can do that with type command.
"type coder.txt"
# we can also make files with type command.
"type nul > coder2.txt"
# but we cant write in that file using type method.
# we will write in coder2.txt file using notepad.
# to open coder2.txt file using notepad we can,
"notepad coder2.txt"
# we can make any type of file using echo command.
"echo >bat.py"
# && allows us to use multiple command at a time.
"echo hello hi bye bye > hello.txt && type hello.txt"

# DEL COMMAND
# del command delete files.
"del hello.txt"
# now lets use multiple command
"echo hello hi bye bye > hello.txt && type hello.txt && del hello.txt"
# we can also use wild cards with del commands too.
"del ?????.txt"
 
# RENAME COMMAND
# we can raname the folders using rename command.
"rename bye hello"
# here we have to write the previous name first and then the new name.
# we can raname the files also.
"rename coder2.txt code.txt"

# Xcopy command
# we can copy files using xcopy command.
'xcopy hello goal\hello /s'
# first we have enter the location of the source file, then we have to write the location that we want to copy, destination. 
# we have to also use the sub-command /s. it will copy the children files and folders too.
# then it will ask that it is a file or directory.
# we will answer that question and our file is copyied.

# Move command
# move command is use for cut files form one destination to another.
"move code.txt goal"
# we can move it back
"move goal\code.txt"
# we dont have to write any destination, then it will automatically move to our current destination.

# PROMPT COMMAND
# prompt command can change the location which is currently terminal using.
"prompt terminal:"
# then instead of seeing C:\USsers\User we will see terminal:
# if we want to make it default then we can write promp again.
"prompt"

# prompt has some special codes.
# lets see them
"prompt /?"

# Changes the cmd.exe command prompt.

# PROMPT [text]

#   text    Specifies a new command prompt.

# Prompt can be made up of normal characters and the following special codes:

#   $A   & (Ampersand)
#   $B   | (pipe)
#   $C   ( (Left parenthesis)
#   $D   Current date
#   $E   Escape code (ASCII code 27)
#   $F   ) (Right parenthesis)
#   $G   > (greater-than sign)
#   $H   Backspace (erases previous character)
#   $L   < (less-than sign)
#   $N   Current drive
#   $P   Current drive and path
#   $Q   = (equal sign)
#   $S     (space)
#   $T   Current time
#   $V   Windows version number
#   $_   Carriage return and linefeed
#   $$   $ (dollar sign)

# If Command Extensions are enabled the PROMPT command supports
# the following additional formatting characters:

#   $+   zero or more plus sign (+) characters depending upon the
#        depth of the PUSHD directory stack, one character for each
#        level pushed.

#   $M   Displays the remote name associated with the current drive
#        letter or the empty string if current drive is not a network
#        drive.

# lets see the time instead of the location.
# we can use the $T sub command.
# to see the greater than sign we need to use $G.
"prompt $T$G"
# if we want to see equal to we can use &Q
# for space we can use $S
"prompt $Q$S$G" 
# we can also make the python idle sign.
"prompt $G$G$G"
# we can customize the terminal like this.

# Title command
# we can change the title with the title command.
"title AS8_CommandAssistant"

# to exit command prompt we can use.
"exit()"