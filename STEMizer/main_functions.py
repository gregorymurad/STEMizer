import json

def save_to_file(data,filename):
    with open(filename,'w') as write_file:
        json.dump(data,write_file,indent=2)
        print("The file {0} was successfully created.".format(filename))

def read_from_file(filename):
    with open(filename,'r') as read_file:
        file=json.load(read_file)
        print("You successfully read from {0}.".format(filename))
        return file

