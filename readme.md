Description:

parse.py is used to parse through trace-*.json files and it store both parent and children information. The children are found against a name eg -rpc,db, wsgi etc. both information of child and its parent will be stored in another json file in the same directory with the name <jsonfilename>_<childname>_filtered.
Eg. trace-boot-and-associate-floating-ip.json_rpc_filtered.
the json file which needs to be traced should be in the same directory.

Arguments to be passed:

1. the json file -filename
2. name of filter -name



Code Syntax:

pip install -r requirement.txt

python parse.py -filename <filename> -name <name>


Example:

python parse.py -filename trace-create-and-delete-image.json -name rpc
