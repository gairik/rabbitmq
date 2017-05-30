import json

#File name needs to be edited here
f = open("<File-name>.json","r")
s = f.read()

input = raw_input()
input = input.strip()

def predicate():
    return input



trace = json.loads(s)
links =[]

def parse(trace):
    children = trace.pop("children",[])
    for child in children:
        parse_aux(trace,child)


def parse_aux(parent,child):
    gchildren = child.pop("children",[])

    for key,value in child.items():
        if type(value)==dict:
            if value.get("name")==predicate():
                links.append({"parent":parent,"child":child})

    for gchild in gchildren:
        parse_aux(child,gchild)

parse(trace)
#for i in links:
#    print i

print json.dumps(links)
