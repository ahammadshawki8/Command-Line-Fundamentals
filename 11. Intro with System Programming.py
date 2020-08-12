# General Intro with system programming:

# system programming is one of the concepts of advanced python
# python has many modules and tool to work with system programming very easily.
# sys programming:
    # it is programming for system based softwares. 
    # it deals the programming that is often part of the operating system.
    # in this module, we will learn pipes, threads, folks and so on about system programming

    

# Detail Intro to SYSTEM PROGRAMMING:

# what is system programming(SP)?
# the activity of programming system components or system software.
# system programming provides and services to the computer hardware.
# where as application programming produce a software which provides tools or services to the user.

# system focussed programming is actually done in python by sys and os module.
# python is well suited for system programming or even platform independent system programming as well.
# the advantage of python in sys programming are-
    # 1. it is simple and clear
    # 2. it is well structured
    # 3. it is highly flexible

# sys module:
# first we need to import the sys module of python to work with system.
import sys
# sys modules provides information about constances, functions, methods 
# and all of the python interpreter presents in the machine.

# to see all the attributes, methods, class in sys module we can use the dir method.
print(dir(sys))
# another possibility is to use the help function incase we dont know anything about the module.
#print(help(sys))
# we can see the python version with version attribute
print(sys.version) 
# to see more info about python version we can, 
print(sys.version_info)

# lots of scripts woll need access to the arguements pass to the script when it was started.
# we need something called ARGV or more precisely we call it sys.argv
# here ARG stands for arguement and V stands for Variable. 
# it is basically a list which contains all of the command line arguements pass to the script.
#  the first line of this script contains the name of the script itself and the arguements follows the script name.
print(sys.argv)
# it can be iterated via a loop
for i in range(len(sys.argv)):
    if i==0:
        print(f"Function name: {sys.argv[0]}")
    else:
        print(f"    {i}. Argument name : {sys.argv[1]}")

# python's interective mode is one of the things which makes python special than any other language.
# it is eniugh to write a expression over the command line to get back a meaninggul output.
# however, some users might prefer a different output behaviour.
# well to change the behaviour how the interpreter prints interectively using the introde expressions,
# we will actually need to rebind the sys.displayhook to a callable object.
# we need to use the command line.
"""
>>> x=88
>>> x
88
>>> def my_display(x):
...     print("out: ", x)

>>> sys.displayhook=my_display
>>> x
out: 88
>>> print(x)
88
"""
# note that here behaviour of print() not changed.
# here we can change the output behaviour without changing the behaviour of a function.

# every series user of linux and unix operating system knows the standerd stream right
# there are stdin, stdout, stderr. they are also knows as "pipes".
# stdin is normally connected to the keyboard whereas
# stdout and stderr actually connected to the terminal or the window that we are currently working.
# these three streams can be acsessed in python and the object of the sys module have the same name.
for i in (sys.stdin, sys.stdout, sys.stderr):
    print(i)

# # #
print("going via stdout")
sys.stdout.write("Another way of printing\n")

x=input("Reading value via stdin: ")
print(x)
print("Another way to type in value: ", sys.stdin.readline()[:-1]) # here the slicing because of skipping extra newlines.
print(x)

# redirections:
# there is hardly any user of linux and unix shell dont use redirections
# no useful works can done without redirections.
# the stdout can be redirected into a file so that we can process that file later and use that within another programm.
# the same is possible with the stderr stream.
# we can redirect the stdout and stderr in the same file or in separate files if we want to.

# redirecting stdout:
print("Coming Through Stdout!!")

# saving stdout
save_stdout=sys.stdout

with open("F:\\Python\\# Files Created by Python\\TestX.txt","w") as fh:
    sys.stdout = fh
    print("This line wont print")
    sys.stdout.write("It will go to TestX.txt too")

# return to normal
sys.stdout=save_stdout

print("Now we are Back!!")

# redirecting stderr:
save_stderr=sys.stderr

with open("F:\\Python\\# Files Created by Python\\errorX.txt","w") as eh:
    sys.stderr=eh
    #x=10/0
    #p=int("f")

sys.stderr=save_stderr

# variables and constants in sys module
# we have some variables in sys module. they are-
# byteorder, executable, maxsize, modules, path, platform and many more.
print(sys.byteorder) # indicator of native byteorder.
print(sys.executable) # a string contsining the executable binary. it means the path and execuatble binary for that current python interpreter.
print(sys.maxsize) # this variable largest possible integer which supported by python regular integer type.
print(sys.modules) # the value of sys.modules actually is a dictionay mapping.
# it maps the names of the modules to the modules which we already being located and this can be manipulated.
# for example, we can enforce the reloading of modules as well.
print(sys.path) # path contains a search path where python is looking for all of the modules that are present.
print(sys.platform) # platform gives us the name of the platform on which python is running on. it is linux2 for linux and win32 for windows.

# python and the shell
# what is shell?
# A piece of software that provides a interface for a user to some other software or the operating system.
# shell can be 2 types.
    # 1. command line interpace (CLI). in most cases, shell means cli. some cli's are-
        # (i)    bash
        # (ii)   powershell
        # (iii)  cmd 
        # (iv)   C-shell
        # (v)    Bourne shell (SH). it is the first unix shell.
    # 2. graphical user interface (GUI)

# most operating system's shell can be used both interactive mode and in batch mode (COI) as well.
 

# os module:
# what is os module?
# the os module is a module which allows platform independent programming by providing abstract methods.
# it is the most important module to interect with the operating system.
# it is also possible by using the system function and the exec*() function.
# this family includes system independent programme part as well.

# os module provides various function that can do many thing such as accessing the file stream which is a very important thing.
# it is not possible in python to read a character without type the return key.
# on the other hand it is extreamly easy to do this in the bash shell.
# the bash commands actually read (n-1) weight keys for any key which is inputed by the user.
# if we import os, it is really easy to write a script providing getch() by using os.system() function and the bash shell.
# getch() actually weights just one character to be typed without return.
import os

# this works in linux
# def getch():
#     os.system("bash -c \"read -n 1\"")

# getch()

# for windows we can,
import msvcrt
msvcrt.getch()

# now lets see a  scripts which implement an independent solution to our problem.
# it is actually the platform independency.
import os, platform

if platform.system() == "Windows":
    import msvcrt

def getch():
    if platform.system()=="Linux":
        os.system("bash -c \"read -n 1\"")
    else:
        msvcrt.getch()

print("Type any key!")
getch()
print("Okay")

# forking in python
# trees are actually a example of forking.
# long before when biologist started research of clonning, comp. scientist had a successful history of clonning.
# but they dont called clonning, they called forking.
# it is one of the important aspects of unix and linux.
# when a process forks it actually creates a copy of itself. then the process called parent thread and its copy called child thread.
# in general, fork is actually in a mutli-threading environment which means that a thread of execution is duplicated.

# parent thread and child thread are identical but definately can be told apart.
# they can told apart by the process id.
# fork operation creates a separate address for child and parent.
# child process has an exact copy of all of the memories of the parent process.
# the execution of parent and child process is independent to each other.

# in computer science, the term fork stands for 2 different aspects.
# the first one is clonning of a process.
# and in software enginneering a project fork happens with the developers take a legal copy of source code from one software package 
# and start independent development on it. 

# in system function the term fork actually create a copy of a process which it has been called for.
# this copy is runs as the child process of the calling process.
# the child process get the data and the code form the parent process.
# the child process receives a process number which is called process id (PID) from the operating system.
# the child process runs as a independent instance.
# with the return of fork, we can actually decide in which process we are.
# 0 means we are in the child process and 1 means we are in the parent process.
# a negative return value means a error occured when we tried to fork.

# to fork the process we need os module.
import os

def child():
    print("\nA new Child ", os.getpid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pids=(os.getpid(),newpid)
            print("parent: %d, child: %d\n" %pids)
        reply = input("will you want a new fork? (y/n)")
        if reply == "y":
            continue
        else:
            break

parent()

# the exec*() functions
# forks are of new to start independent programs
# to do this we need to use the exec*() functions.
# the execute a new program by replacing the current process of that program.
# they do not return to the program which has called them.
# they even get the same processs id as the calling process.
# there are variety of exex*() function. some of them are-
    # os.execl()
    # os.execle()
    # os.execlp()
    # os.execlpe()
    # os.execv()
    # os.execve()
    # os.execvp()
    # os.execvpe()

# threads in python
# what is a thread?
# the smallest unit that can be scheduled in an operating system.
# threads are normally created by a fork statement of a computer script or a program.
# these can be implemented in single processor by multitasking as well.
# more than one thread can exists within the same process.
# these threads share the memory and the state of process as well.
# on the other words, they actually share the code and the value of the variables of the process.

# threads can be of 2 kinds
    # Kernal threads: implemented in kernal. it is a part of the operating system.
    # user threads: not implemented in kernal
    # it is pretty simmilar to a function or a prosedure call. but they have some difference to the regular function specially in the return behaviour.

# every process need to have one thread.
# the process itself is a thread.
# a process can starts multiple threads.
# the operating system executes this threads in parralal process.
# and in a single processer machine, this parallelism is achieved by thread sceduling or time slicing.

# what are the advantage of threading?
# multi threaded program can run faster in computer system with multiple cpus because this threads can be execute trully concrately.
# they can run parallelly in true form. 
# a program can remain responsive to the input as well. this is true both on single and multiple cpu.
# threads of a process can share the memory of a global variable too.
# if a global variable change one thread it will be valid for all other threads.
# threads can have local variable as well.
# handling of threads is really simpler than handling of the processes in any operating system.
# that why they sometime called light way process (LWP)

# there are two modules of python which supports threading. they are
    # thread. it is considered as depricated for quite long time.
    # threading. users generally use threading module instead of thread module.
# in python3, thread module is renamed as _thread for backward compitability.
# module thread treats a thread as a function.
# module threading implements in a oop way. here every threads correspond to one perticular object.

# thread module
# it is possible to execute functions with a separate thread in the thread module.
# to do this we can
from _thread import start_new_thread

num_threads=0
def heron(a):
    """Calculates the square root of a"""
    eps=0.00000001
    old=1
    new=1
    while True:
        old,new =new, (new +a/new) /2.0
        print(old,new)
        if abs(new-old) <eps:
            break
    
        global num_threads
        num_threads +=1

    # code has been left out, see above
        num_threads -=1
    return new

start_new_thread(heron,(99,))
start_new_thread(heron,(999,))

while num_threads >0:
    pass
# here it takes the function name and the arguement of that function in a tuple.

q=input("Type somethign to quit")
# this input is necessary.
# because otherwise all the threads would be exited in the same time if the main program finishes.

# this exmaple can make some errors.
# the problem is that in the final while loop we will be reached before one of the threads implemented before the counter.
# in our case, the counter was num_threads.
# there is another problem
# the threads rises by assignments to num_thread. num_thread+=1 and num_thread-=1.
# this assignment statements are not atomic.
# atomic statements consist of three actions.
# it starts with reading the value of num_thread
# then we have a new intinstance which can be incremented or decremented by 1.
# then the new value has to be assigned to num_threads.
# error like this actually happen in the case of increment or decrement.
# first thread reads the variable num_thread which still has the value of 0
# after having read the value the thread will put to sleep by the operating system.
# now, the second thread reads the value of the variable num_thread which is again still 0
# because of the first thread has been put to sleep too early even it has given the chance to increment by 1.
# now second thread will put to sleep.
# then the third thread come which again reach 0. but the counter should have reached 2 by now.
# simmilarly the problem occurs with the decrement.


# but we can solve this problems by defining critical sections of lock objects.
# this section will be treated automatically.
# while during the execution of such a section, a thread will not be interapted or put to sleep.

# the method thread.allocate_lock() is actually used to create a new object.
# lock_object=thread.allocate_lock()
# and the beginning of a critical section is actually tagged with lock_object.aquire() and end with lock_object.release()

# so the solution is like-
from _thread import start_new_thread,allocate_lock
num_threads=0
thread_started=False
lock =allocate_lock()

def heron2(a):
    """Calculates the square root of a"""
    eps=0.00000001
    old=1
    new=1
    while True:
        old,new =new, (new +a/new) /2.0
        print(old,new)
        if abs(new-old) <eps:
            break
    
        global num_threads,thread_started
        lock.acquire()
        num_threads += 1
        thread_started=True
        lock.release()

        ...

        lock.acquire()
        num_threads -= 1
        lock.release()

        num_threads -=1
    return new

start_new_thread(heron2,(99,))
start_new_thread(heron2,(999,))

while not thread_started:
    pass
while num_threads>0:
    pass

# threading module
# thread module doesn't do a lot
# method of operation threading.thread class is very interesting.

# the class threading.thread has a method called start() which start a thread.
# it triggers of the method run() which has to be overloaded again.
# ones overloaded the join() method ensures the mainprogramme waits until all of the threads are dominated.

# Pipes in python
# what are pipes?
# Inroducing modularity in the program to serve one instance output as the input to another instance and so on till solution is achieved.
# without pipes, unix and linux are unthinkable.
# pipelines are important part of unix and linux application and architecture.
# small commands are put together through pipes.
# processes are changed together by their standerd stream.
# it means the output of one process chains to the input to the next process.
# this chains are called anonymous pipes.

# generally, there are actually 2 kinds of pipes.
    # Anonymous pipes: exists solely within processes and are usualyy used in combination with forks.
    # named pipes

# named pipes 
# what are named pipes?
# creating pipes which are implemented as files. sometimes called first in first out (FIFOs)
# so a process reads and writes to such a pipe as if it is were regular file.
# sometimes more than 1 process writes to a pipe but only one process can read from it at a time. 

# there is so much more we can do with pipes.
