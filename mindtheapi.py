import argparse
import xml.etree.ElementTree as ET
from re import search

def print_line(i, req_methods, path):
    print(i*'#', req_methods, path)

def create_markdown(data):
    levels = []
    for path in sorted(data):
        for i, lvl in enumerate(path.split('/')):
            if i == 0:
                continue
            split = path.split('/')
            req_methods = ""
            if len(split) == i+1:
                for method in data[path]:
                    req_methods += method + '&'
                req_methods = req_methods[:-1]
            if len(levels) < i:
                levels.append(lvl)
                print_line(i, req_methods, lvl)
            elif levels[i-1] != lvl:
                levels[i-1] = lvl
                print_line(i, req_methods, lvl)

def parse_text(filename):
    data = {}
    with open(filename) as file:
        for line in file:
            split = line.split(' ')
            stripped_path = ' '.join(split[1].split()) # removes new lines, spaces etc
            reg_find = search("^.*?(?=[&,?,#])", stripped_path) # extracts the path
            if reg_find:
                stripped_path = reg_find.group(0)
            if stripped_path in data:
                data[stripped_path].add(split[0])
            else:
                data[stripped_path] = {split[0]}
    return data

def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for item in root.findall('item'):
        meth = ""
        for child in item:
            if child.tag == "method":
                meth = child.text
            if child.tag == "path":
                reg_find = search("^.*?(?=[&,?,#])", child.text) # extracts the path
                cleaned_path = child.text
                if reg_find:
                    cleaned_path = reg_find.group(0)
                if cleaned_path in data:
                    data[cleaned_path].add(meth)
                else:
                    data[cleaned_path] = {meth}
    return data

def main():
    parser = argparse.ArgumentParser(description='Create markdown of the API')
    parser.add_argument('-x', "--xml", metavar="file", help='input as XML')
    parser.add_argument('-t', "--txt", metavar="file", help='input as txt')
    args = parser.parse_args()

    data = {}
    if args.txt:
        data = parse_text(args.txt)
    elif args.xml:
        data = parse_xml(args.xml)
    else:
        parser.print_help()

    create_markdown(data)

if __name__ == "__main__":
    main()
