import sys
sys.path.insert(0, './includes')
import functions as fn

if fn.sysTest()==False:
    sys.exit("System test: FAILED")

print("System test: OK")

