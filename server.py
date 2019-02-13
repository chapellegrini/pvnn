#! /usr/bin/env python3
# -- coding:utf-8 --

# This file serves the website and handles requests.
# It should be run with the command : "python -m flask run" after defining
# the location of the file with "export FLASK_APP = path" or "set" on Windows.

from flask import Flask, request, send_from_directory, redirect, url_for
from request_to_dict import *
from generate_javascript_layers import *
from generate_python_from_graph import *
from flask import Response
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
# from multiprocessing import Process, current_process
import urllib.parse


app = Flask(__name__, static_url_path='/grapheditor', static_folder='grapheditor')
layers_js = generate_js()

'''
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per minute", "1 per second"],
)'''

# Ban list works with the limiter but the WSGI developpement server does not allow a correct multithreaded control of the generate function,
# so it will return in the next version with propably an nginx server.
# ban_list = ["127.0.0.1"]

# Main page route redirecting to the index page
@app.route('/')
def redirect_index():
	return redirect('/grapheditor/www/index.html')


# The route that allows to serve the dynamically created "layers.js"
@app.route('/generated/layers.js', methods=['GET'])
def generate_layers():
    return layers_js

# The save route allows the user to save the graph as a XML file or as a SVG file.
# The SVG save format is reachable by the "export" menu in GraphEditor.
@app.route('/save', methods=['POST'])
#@limiter.limit("1 per day", exempt_when=lambda:get_remote_address() not in ban_list)
def save_xml():
    print(request.args)
    print('\n')
    print(request.form)
    print('\n')
    print(urllib.parse.unquote(request.form['xml']))
    filename = urllib.parse.unquote(request.form['filename'])
    extension = ".xml"
    if filename[-4:] == '.xml':
        filename = filename[:-4]
    elif filename[-3:] == '.py':
        filename = filename[:-3]
    elif filename[-4:] == '.svg':
        filename = filename[:-4]
        extension = ".svg"


    # The save method is also used by GraphEditor to create a *.svg record of the graph
    return Response(bytes(urllib.parse.unquote(request.form['xml']),'utf-8'),
                       mimetype="text/xml",
                           headers={"Content-Disposition":
                                    "attachment;filename="+filename+extension})

# The generate route allows the user to create the python file from the graph.
# It calls an extern function which create a dict object from the post data, which will be easier to manipulate after.
# Then it returns a python file. The "generate_graph_from_dict" is only a minimalist version of the function that will be called,
# and it only works with a correct graph (for example: Input -> Conv2D -> Output)
@app.route('/generate', methods=['POST'])
#@limiter.limit("1 per day", exempt_when=lambda:get_remote_address() not in ban_list)
def generate_python():
    print(request.form)
    print('\n')
    print(urllib.parse.unquote(request.form['xml']))
    print('\n')
    filename = urllib.parse.unquote(request.form['filename'])
    if filename[-4:] == '.xml':
        filename = filename[:-4]
    elif filename[-3:] == '.py':
        filename = filename[:-3]
    # ip = get_remote_address()
    graph = request_to_dict(urllib.parse.unquote(request.form['xml']))
    return Response(generate_python_from_graph(graph),
   	                  mimetype="text/plain",
   	                  headers={"Content-Disposition":
                                    "attachment;filename="+filename+".py"})


# the "/open" page is called whenever grapheditor is refreshed.
# It does not need to do something in particular, but to have a return argument.
@app.route('/open', methods=['POST'])
def open_file():
   return('hello')

if __name__ == '__main__':
    app.run(threaded=True)
    # Debug mode has to be desactivated for the release.
