# generate_javascript_layers.py
# Script that generates a javascript file named layers.js
# This is done via a list of hardcoded layers to translate into the correct format
# The file thus generated is then served to clients to be used by the javascript interface,
# allowing easier maintenance of the software

# Built-in activation functions - see keras/activations.py
# some of them can take additional options


#class Options(object):
#    type =

from keras_layers import *

def _get_js_varname(layer):
    return 'layer'+layer

def _get_js_param_varname(layer, param):
    return _get_js_varname(layer) + 'Param' + param

def generate_rawlayer(layer, group):
    varname = _get_js_varname(layer)
    str  = 'var '+varname+' = new KerasLayer(\''+layer+'\',\''+group+'\')\n'
    #str += varname+'.searchTerm = "'+layer+'";\n';
    return str

def generate_unimp(layer, paramName, paramData):
    layerVarname = _get_js_varname(layer)
    paramVarname = _get_js_param_varname(layer, paramName)
    str = 'var ' + paramVarname + ' = new KerasParameter("'+paramName+'"); // Unimplemented Type\n'
    str += layerVarname+'.addParameter('+paramVarname+');\n'
    return str

def generate_int(layer, paramName, paramData):
    layerVarname = _get_js_varname(layer)
    paramVarname = _get_js_param_varname(layer, paramName)
    str = 'var ' + paramVarname + ' = new KerasParameterNumeric("'+paramName+'");\n'
    str += layerVarname+'.addParameter('+paramVarname+');\n'
    if 'step' in paramData:
        str += _get_js_param_varname(layer, paramName) + '.setStep('+paramData['step']+');\n'
    else:
        str += _get_js_param_varname(layer, paramName) + '.setStep(1);\n'
    if 'conditions' in paramData:
        for condition in paramData['conditions']:
            print(condition)
            if condition[0:2] == '<=':
                str += paramVarname + '.setMaximum(' + condition[2:] + ',true);\n'
            elif condition[0:2] == '>=':
                str += paramVarname + '.setMinimum(' + condition[2:] + ',true);\n'
            elif condition[0] == '<':
                str += paramVarname + '.setMaximum(' + condition[1:] + ',false);\n'#TODO: INVALID IF EQUAL
            elif condition[0] == '>':
                str += paramVarname + '.setMinimum(' + condition[1:] + ',false);\n'#TODO: INVALID IF EQUAL
    return str

def generate_list(layer, paramName, paramData):
    layerVarname = _get_js_varname(layer)
    listName = _get_js_param_varname(layer, paramName)
    listElements = paramData['list']

    str = 'var ' + listName + ' = new KerasParameterList("'+paramName+'");\n'
    str += layerVarname+'.addParameter('+listName+');\n'

    for listEl in listElements:
        listElVarname = listName + listEl
        str += 'var '+listElVarname+' = new KerasParameterListElement("'+listEl+'");\n'
        str += listName+'.addListElement('+listElVarname+');\n'
    return str

def generate_float(layer, paramName, paramData):
    str = generate_int(layer, paramName, paramData)
    str += _get_js_param_varname(layer, paramName) + '.setTypeToFloat(true);\n'
    if 'step' not in paramData:
        str += _get_js_param_varname(layer, paramName) + '.setStep(0.1);\n'
    return str

def generate_tuple_int(layer, paramName, paramData):
    layerVarname = _get_js_varname(layer)
    paramVarname = _get_js_param_varname(layer, paramName)
    s = 'var ' + paramVarname + ' = new KerasParameterTuple("'+paramName+'");\n'
    if 'elements_number' in paramData:
        elements_number = paramData['elements_number']
        s += paramVarname + '.setElementsNumber('+str(elements_number)+');\n'
    if 'elements_max_number' in paramData:
        elements_max_number = paramData['elements_max_number']
        s += paramVarname + '.setElementsMaxNumber('+str(elements_max_number)+');\n'
    if 'elements_min_number' in paramData:
        elements_min_number = paramData['elements_min_number']
        s += paramVarname + '.setElementsMinNumber('+str(elements_min_number)+');\n'
    s += layerVarname+'.addParameter('+paramVarname+');\n'
    print(s)
    return s

def generate_param_multiplexer(layer, paramName, paramData):
    if(paramData['type'] in generate_types):
        return generate_types[paramData['type']](layer, paramName, paramData)
    print("Param not implemented : " + paramData['type'])
    return generate_unimp(layer, paramName, paramData)

generate_types = {'int': generate_int,
                  'list': generate_list,
                  'boolean': generate_unimp,
                  'float': generate_float,
                  'tuple_int': generate_tuple_int,
                  'string': generate_unimp,
                  'function': generate_unimp,
                 }

def generate_layer(layer, group, parameters = {}):
    rs = generate_rawlayer(layer, group)
    for parameter in parameters:
        rs += generate_param_multiplexer(layer, parameter, parameters[parameter])
    return rs

def generate_layers(layer_dict, category_name):
    rs = ''
    for layer, parameters in layer_dict.items():
        rs += generate_layer(layer, category_name, parameters) + '\n\n'
    return rs

def generate_js():
    rs = '' # return string
    rs += generate_layer('Input', 'Input / Output', keras_core_layers['Input']) + '\n\n'
    rs += generate_layer('Output', 'Input / Output') + '\n\n'
    for layer, parameters in keras_core_layers.items():
        if(layer == 'Input'):
            continue
        rs += generate_layer(layer, "Core Layers", parameters) + '\n\n'
    for category_name, layer_dict in keras_layers_categories.items():
        rs += generate_layers(layer_dict, category_name)

    #print(rs)
    return rs
