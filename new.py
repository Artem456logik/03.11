print("Hello, guys from new file!")

import sys

args = sys.argv
print(args)

second_arg = args[1]
#переписати використовуючи словник
if second_arg == "1":
    print("Hello, World!")
elif second_arg == "2":
    print("Hello, everyone!")
elif second_arg == "3":
    print("Hello, my teacher!")
else: 
    print("Hello, no one")