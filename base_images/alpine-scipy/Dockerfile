# ==================== #
# Compile dependencies #
# ==================== #
FROM python:3.6-alpine AS base

ARG PANDAS_VERSION=0.23.0
RUN apk add --no-cache \
        --virtual=.build-dependencies \
        g++ gfortran file binutils gcc \
        musl-dev python3-dev openblas-dev libstdc++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip wheel --wheel-dir=/root/wheels numpy==1.14.0 pandas==${PANDAS_VERSION} && \
    pip install --no-index --find-links=/root/wheels numpy pandas

RUN pip wheel --wheel-dir=/root/wheels scipy

# ============================================== #
# Build release image, with minimal dependencies #
# ============================================== #
FROM python:3.6-alpine

# add openssh, git and misc. runtime requirements
#   numpy requires openblas, pandas requires libstdc++
#   librdkafka is not required but speeds things up
RUN apk add --no-cache git openssh openblas libstdc++ librdkafka

# set up paths for ssh key runtime secret named 'deploy_key'
RUN mkdir -p /run/secrets && \
    mkdir -p /home/app/.ssh && \
    touch /run/secrets/deploy_key && \
    ln -s /run/secrets/deploy_key /home/app/.ssh/deploy_key

ADD config /home/app/.ssh/config

RUN addgroup -g 1000 -S app && \
    adduser -u 1000 -S app -G app && \
    chown -R app:app /home/app
USER app

# add path used by pip to PATH
ENV PATH $PATH:/home/app/.local/bin

COPY --chown=app:app --from=base /root/wheels /home/app/wheels
RUN pip install --user --no-index --find-links=/home/app/wheels numpy pandas scipy

# set git author and email
RUN git config --global user.email "andbberger@gmail.com" && \
    git config --global user.name "Andrew Berger"
