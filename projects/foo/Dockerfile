FROM rueberger/alpine-scipy:latest

# NOTE: the purpose of installing requirements.txt in a separate layer is to improve caching between builds
# requirements.txt doesn't change very often, so this layer will usually be cached
ADD --chown=app:app requirements.txt  /home/app/foo/requirements.txt
RUN pip install --user --find-links=/home/app/wheels --cache-dir=/home/app/wheels -r /home/app/foo/requirements.txt

ADD --chown=app:app . /home/app/foo
RUN pip install --user --no-index --find-links=/home/app/wheels --cache-dir=/home/app/wheels -e /home/app/foo/
