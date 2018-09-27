FROM docker.elastic.co/beats/filebeat:6.2.4

USER root
RUN yum -y --enablerepo=extras install epel-release && \
    yum -y update && \
    yum -y install python-pip && \
    pip install elasticsearch-curator

RUN mkdir -p /usr/share/filebeat/.curator

# set up volume permissions
RUN mkdir -p /filebeat_data && \
    chown filebeat:filebeat /filebeat_data && \
    mkdir -p /logs && \
    chmod -R a+rw /logs && \
    mkdir -p /var/log/filebeat && \
    chown filebeat:filebeat /var/log/filebeat

USER filebeat
