parse.py is used to parse through trace-*.json files and it store both parent and children information. The children are found against a name eg -rpc,db, wsgi etc. both information of child and its parent will be stored in another json file in the same directory with the name <jsonfilename>_<childname>_filtered.
Eg. trace-boot-and-associate-floating-ip.json_rpc_filtered.
the json file which needs to be traced should be in the same directory.

Two information required to be given while calling parse.py are
1. the json file which needed to be parsed. -filename
2. the child name. -name


before running parse.py. you need to do from terminal

pip install -r requirement.txt
python parse.py -filename <filename> -name <name>
