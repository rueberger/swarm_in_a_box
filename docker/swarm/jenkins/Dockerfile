FROM jenkins/jenkins:2.132-slim

# add jenkins user to sudoers so jenkins can use docker
USER root
RUN apt-get update && \
    apt-get install -y sudo libltdl-dev make && \
    rm -rf /var/lib/apt/lists/*

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
