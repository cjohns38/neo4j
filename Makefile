run:
	docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$$HOME/neo4j/data:/data \
    neo4j

docker_pull:
	docker pull neo4j
