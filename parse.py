"""
Usage:
  my_prog2.py -filename <x> -name <y>

Options:
  -h --help     Show this screen.

"""

from docopt import docopt
import json
import os

def parse(trace,pred):
    f = open(trace,"r")
    trace = f.read()
    trace = json.loads(trace)

    children = trace.pop("children",[])
    for child in children:
        parse_aux(trace,child,pred)


def parse_aux(parent,child,pred):
    gchildren = child.pop("children",[])

    for key,value in child.items():
        if type(value)==dict:
            if value.get("name")==pred:
                links.append({"parent":parent,"child":child})

    for gchild in gchildren:
        parse_aux(child,gchild,pred)



if __name__ == '__main__':


    arguments = docopt(__doc__, version='my prog 2.0')
    path =  (arguments.get("<x>"))
    pred = (arguments.get("<y>"))

    links=[]
    parse(path,pred)
    t =  os.getcwd()


    #os.mkdirs(res )
    path = path + "_"+ pred + "_filtered"

    obj =  json.dumps(links)
    file = open(path, 'w')
    file.write(obj)
    file.close()
