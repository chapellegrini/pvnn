#!/usr/bin/env python3

import urllib.parse
import xml.etree.ElementTree as ET
import base64
import json

def parse_cell_data(data_field):
    parsed_data = ET.fromstring('<data>' + data_field['string'] + '</data>')#add <data> so we can parse html as xml
    for n in parsed_data:
        if n.tag == 'h3':
            data_field['title'] = n.text
        if n.tag == 'p':
            data_field['param'] = json.loads(base64.b64decode(n.text).decode('utf-8'))

def request_to_dict(request_dict):
    """Convert a request dict to an improved dictionary

    The request string corresponds to the quoted body of a POST request.
    The dict returned contains the different nodes, including their sources,
    targets, and data.
    """
    #:DELETED:CHATELAIN:28/03/2018:
    # These 2 lines are useless now that flask is able to convert the request to a proper dict on the main server file
    # file_description = urllib.parse.parse_qs(request_string)
    # xml = urllib.parse.unquote(file_description['xml'][0])
    #:TODO:PELLEGRINI:16/02/2018:
    # https://docs.python.org/2/library/xml.html#xml-vulnerabilities
    # vulnerable to billion laughs and quadratic blowup...
    mxgraph_model = ET.fromstring(request_dict)

    root = mxgraph_model[0]
    result = {}
    def add_node(node_id):
        result[node_id] = {'sources' : [], 'targets' : [], 'data' : {}, 'treated' : False}
    for child in root:
        #print(child.tag, child.attrib)
        if child.tag == 'mxCell':
            if 'vertex' in child.attrib:
                if child.attrib['vertex'] == '1':
                    node_id = child.attrib['id']
                    if node_id not in result:
                        add_node(node_id)
                    if 'string' not in result[node_id]['data']:
                        result[node_id]['data']['string'] = child.attrib['value']
                        parse_cell_data(result[node_id]['data'])
            if 'edge' in child.attrib:
                if child.attrib['edge'] == '1':
                    source = child.attrib['source']
                    target = child.attrib['target']
                    if source not in result:
                        add_node(source)
                    if target not in result:
                        add_node(target)
                    result[source]['targets'] += [target]
                    result[target]['sources'] += [source]
    return result
