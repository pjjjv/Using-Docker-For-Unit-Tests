FROM centos:centos7
MAINTAINER Chris Collins <christopher.collins@duke.edu>

RUN yum install -y python
RUN mkdir /stuff_to_test
ADD script-to-test.py /stuff_to_test/script-to-test.py

WORKDIR /stuff_to_test

ENTRYPOINT [ "python", "script-to-test.py" ]
