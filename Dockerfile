FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install pandas
RUN pip3 install -q plotly
RUN pip3 install dash
RUN pip3 install dash_core_components
RUN pip3 install dash_html_components
RUN pip3 install dash-bootstrap-components
RUN pip3 install Flask

RUN cd opt

COPY main.py .

ENTRYPOINT python3 main.py