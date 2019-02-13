FROM ubuntu

LABEL maintainer="romain.giot@u-bordeaux.fr"
LABEL licence="LGPL"


RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
	apt-get install -qy python3-pip

RUN pip3 install flask
RUN mkdir /pdp

COPY grapheditor /pdp/grapĥeditor/
ADD keras_layers.py request_to_dict.py server.py generate_python_from_graph.py generate_javascript_layers.py /pdp/

WORKDIR /pdp

EXPOSE 5000

RUN ls -R
ENTRYPOINT ["python3", "server.py"]
