#!/usr/bin/env python3

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from request_to_dict import *
from generate_python_from_graph import *

saved_response = '<mxGraphModel dx="1426" dy="839" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" background="#ffffff"><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="2" target="3" edge="1"><mxGeometry relative="1" as="geometry"/></mxCell><mxCell id="8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=0.75;exitY=1;entryX=0.5;entryY=0;jettySize=auto;orthogonalLoop=1;" edge="1" parent="1" source="2" target="4"><mxGeometry relative="1" as="geometry"/></mxCell><mxCell id="2" value="&lt;h3&gt;Input&lt;/h3&gt;&lt;p hidden=&quot;hidden&quot;&gt;e30=&lt;/p&gt;" style="rounded=0;whiteSpace=wrap;html=1;" parent="1" vertex="1"><mxGeometry x="140" y="160" width="120" height="60" as="geometry"/></mxCell><mxCell id="11" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=0.5;exitY=1;entryX=0;entryY=0.5;jettySize=auto;orthogonalLoop=1;" edge="1" parent="1" source="3" target="9"><mxGeometry relative="1" as="geometry"/></mxCell><mxCell id="3" value="&lt;h3&gt;Dense&lt;/h3&gt;&lt;p hidden=&quot;hidden&quot;&gt;e30=&lt;/p&gt;" style="rounded=0;whiteSpace=wrap;html=1;" parent="1" vertex="1"><mxGeometry x="70" y="260" width="120" height="60" as="geometry"/></mxCell><mxCell id="10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=0.5;exitY=1;entryX=1;entryY=0.5;jettySize=auto;orthogonalLoop=1;" edge="1" parent="1" source="4" target="9"><mxGeometry relative="1" as="geometry"><Array as="points"><mxPoint x="354" y="400"/></Array></mxGeometry></mxCell><mxCell id="4" value="&lt;h3&gt;Dense&lt;/h3&gt;&lt;p hidden=&quot;hidden&quot;&gt;e30=&lt;/p&gt;" style="rounded=0;whiteSpace=wrap;html=1;" parent="1" vertex="1"><mxGeometry x="294" y="260" width="120" height="60" as="geometry"/></mxCell><mxCell id="5" value="&lt;h3&gt;Output&lt;/h3&gt;&lt;p hidden=&quot;hidden&quot;&gt;e30=&lt;/p&gt;" style="rounded=0;whiteSpace=wrap;html=1;" parent="1" vertex="1"><mxGeometry x="174" y="510" width="120" height="60" as="geometry"/></mxCell><mxCell id="12" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=0.5;exitY=1;jettySize=auto;orthogonalLoop=1;" edge="1" parent="1" source="9" target="5"><mxGeometry relative="1" as="geometry"/></mxCell><mxCell id="9" value="&lt;h3&gt;Add&lt;/h3&gt;&lt;p hidden=&quot;hidden&quot;&gt;e30=&lt;/p&gt;" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="180" y="370" width="120" height="60" as="geometry"/></mxCell></root></mxGraphModel>'


if __name__ == '__main__':
  graph = request_to_dict(saved_response)
  result = generate_python_from_graph(graph)
  print(result)
  lines = result.splitlines()

  if lines[0] != 'import keras':
    print('no import')
    exit(-1)

  if lines[3] != '    input_2 = keras.layers.Input()':
    print('no imput')
    exit(-1)

  dense3 = '    layer_3 = keras.layers.Dense()(input_2)'
  dense4 = '    layer_4 = keras.layers.Dense()(input_2)'
  if not (((lines[4] == dense3) and (lines[5] == dense4)) or
          ((lines[5] == dense3) and (lines[4] == dense4))) :
    print('Dense layer failed')
    exit(-1)

  add_9_0 = '    layer_9 = keras.layers.Add()([layer_3,layer_4])'
  add_9_1 = '    layer_9 = keras.layers.Add()([layer_4,layer_3])'
  if not ((lines[6] == add_9_0) or (lines[6] == add_9_1)):
    print('Add layer failed')
    exit(-1)

  if lines[7] != '    model = keras.models.Model(inputs=input_2, outputs=layer_9)':
    print('Model failed')
    exit(-1)

  if lines[8] != '    return model':
    print('Return failed')
    exit(-1)
