import sys
sys.stderr.write("This is stderr text!\n")
sys.stdout.write("This is stdout text!\n")

print(sys.argv)

if len(sys.argv) >1:
    for i in sys.argv[1:]:
        print(i)

print("\n\n")

if len(sys.argv) >1:
    for k in sys.argv[1:]:
        print(float(k)+5)