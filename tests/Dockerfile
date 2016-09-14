FROM centos:centos7
MAINTAINER Chris Collins <christopher.collins@duke.edu>

RUN yum install -y python
RUN mkdir /stuff
ADD program.py /stuff/program.py
ADD test.py /stuff/test.py

WORKDIR /stuff

ENTRYPOINT [ "python", "test.py" ]
