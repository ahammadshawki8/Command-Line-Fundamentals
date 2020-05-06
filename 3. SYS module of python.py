# sys module

# sys stands for system.
# it is an important and interesting module.
# it is about the input, output and command line.
# here argv functioanality is very interesting.

# first we need to import sys module
import sys

# now we will look at the difference between sys.stderr and sys.stdout
# for the most part there is no difference. they are pretty simmilar.
# we should keep sys.stderr strictly for error and sys.stdout for everything output.

# first lets write with stderr().
sys.stderr.write("This is stderr text!")
# it good idea to flush()
sys.stderr.flush()
# it just write buffers, if applicable.
# this is not implemented for read-only and non-bloacking streams.

# now lets write with sys.stdout()
sys.stdout.write("This is stdout text!")
# we can see that there is no spacing or newline in output.
# so it is a good habit to add a newline after we are writing with stderr and stdout
print()
sys.stderr.write("This is stderr text!\n")
sys.stdout.write("This is stdout text!\n")

# now lets work with fun stuff argv
# argv stands for argument variable.
# first lets print this.
print(sys.argv)
# we can see that it it printing the path that we are currently working on.

# but what we can do with this is pretty cool we can pass arguements into this python file using our command line which means using any other language.
# so we can use bash, powershell or all kind of coll stuff.
# or we can really establish communication between python and php or perl or whatever language.

# sys.argv() will display all of the arguements.
# first lets make another module with the same code and open that in cmd.
# we can open it by,
"python sys_helpers.py"
# we can see the stderr, stdout text and argv which is just the file name.

# so we told before that argv is just a list of all of the arguements that we passed in the module by python in cmd.
# in agrv, the first value will be the file name.
# first we had opened it with 
"python sys_helpers.py"
# so we only get the file name which is sys_helpers.py because we didn't pass any arguement.

# now we pass agruements by-
"python sys_helpers.py 'hello world!'" 
# now we can see that it has appened hello and world separately in our argv list.
# in order to append them together, we need to use the double quotations (" ")
'python sys_helpers.py "hello world!"'

# now lets do some fun stuff within our module.
if len(sys.argv) >1:
    for i in sys.argv:
        for i in sys.argv[1:]:
            print(i)

# now lets do pass the arguements that we have passed before.
'python sys_helpers.py "hello world!"'
# now we can see here we have printed out arguements alone without the list.

print("\n\n")

# we can also work with the numbers as well.
if len(sys.argv) >1:
    for k in sys.argv[1:]:
        print(float(k)+5)
        # note that we havae to change the arguements to float.

'python sys_helpers.py 10 5 3 4 2' # we can pass multiple arguements like this.

# so we can start manipulating the values that passed in to python.
# and we can use this to pass the values from anything.

# there is lots of usecase of argv and sys module.
# if we need to make a website in python, but dont really want to code in it.
# then we can code in php or javascipt and then we can communicate with python via argv.
# so we can make a function and the param of that function would be sys.argv and then work in that function.
def main(argv):
    print(argv)
    # here we can add all our code.

main(sys.argv[1:])
# so we can use the argv by passing it through the functio or make a class and whatever we like.
# there are lots of more complex and useful attributes and methods in sys module.
# we can learn more about them in the official documentation of python. lets see all the methods that we have in derectory.
print(dir(sys))

# ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__',
#  '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', 
# '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', 
# '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook',
#  'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names',
#  'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode',
#  'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
#  'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval', 
# 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 
# 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion',
#  'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules',
#  'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks',
#  'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setprofile', 'setrecursionlimit',
#  'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook',
#  'version', 'version_info', 'warnoptions', 'winver']

# we will go through this module describely later if we want to use them in my projects.
# we can also see the system programming module for more information.
