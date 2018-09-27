# Example docker swarm deployment

Fully working single-node deployment of some essential services.

Includes:

- mongo
- kafka
- zookeeper
- redis
- ELK stack
- jenkins

## Usage

1. Build the images: `docker-compose build`
2. Initialize the swarm: `docker swarm init`
3. Deploy: `docker stack deploy --compose-file docker-compose.yml foo_services`
