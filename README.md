# Swarm in a box

Full config for a single-node deployment of many essential devops and data service. Adapted from the production infrastructure used in my now defunct circa 2018 startup. 

## Included services

- mongo
- kafka
- zookeeper
- redis
- ELK stack
- jenkins

## Dev-ops features

- Incremental docker image builds
- New style declarative jenkins pipeline
- Triggers downstream packages on succesful build of master
- hypothesis' example database cached across builds, ensuring previously failed test cases are always rerun.
