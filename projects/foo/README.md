# Example python project, package 'foo'

Simple python package boilerplate. Comes with docker and jenkins integration.

## Features

- incremental docker image builds. Pre-reqs layer only runs when `requirements.txt` changes.
- New style declarative jenkins pipeline
- Triggers downstream packages on succesful build of master
- Configured so that Jenkins caches hypothesis' example database across builds, ensuring previously failed test cases are always rerun.
