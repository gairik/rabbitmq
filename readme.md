parse.py is used to traverse through trace-*.json files.
It looks through all the children and searches for the given name ( eg. rpc) and make a link between the node named rpc and its parent.

The file needs to copied to the same location as that of the json file and the name of the file needs to be edited in the code.
After running the code the console waits for input of name. Once the input is given it starts to find the pair of parent and child of the given name.
