#!/bin/sh

cd /home/app/foo
nosetests --with-xunit --all-modules --traverse-namespace --with-coverage --cover-package=foo --cover-inclusive
pylint -j 0 -f parseable foo > pylint.log

sighup(){
    echo "SIGHUP intercepted (probably because of a failed test). Ignoring"
}
