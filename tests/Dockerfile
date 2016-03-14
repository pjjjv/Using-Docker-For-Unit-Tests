FROM centos:centos7
MAINTAINER Chris Collins <christopher.collins@duke.edu>

RUN yum install -y python
ADD stuff_to_test /stuff_to_test

CMD python /stuff_to_test/script-to-test.py
