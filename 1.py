import sys
import os
import hashlib

if len(sys.argv) < 2:
    print("this script need a arv")
    sys.exit(0)

if not os.path.exists(sys.argv[0]) or not os.path.isdir(sys.argv[1]):
    print("it is not exists or not a dir")
    sys.exit(1)

