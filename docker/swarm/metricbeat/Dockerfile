FROM docker.elastic.co/beats/metricbeat:6.2.4

# add metricbeat user to sudoers so it can access the docker socket
USER root
RUN groupadd docker && \
    usermod -aG docker metricbeat

USER metricbeat
