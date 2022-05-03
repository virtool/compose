# Compose for Virtool

This repository provides a Docker Compose configuration for Virtool development.


## Concepts

Running these services allows you to run Virtool locally.

### Bind Mounts

Bind mounts are paths on the Docker host whose contents are mounted into a Docker container.

Using bind mounts for the Virtool `data_path` allows you to share data between services running in containers and the service you are developing on the host.


## Using

1. Clone the repository:

   ```sh
   https://github.com/virtool/compose.git
   ```
   
2. Change the bind mount sources to match your own environment.

   For example, change `/home/igboyes/Projects/compose/data` to `/home/bob/virtool_data`.

3. Start services using a project name (`-p`) and profile (`--profile`):

   ```sh
   docker-compose -p virtool --profile ui up -d
   ```


## Profiles

| Name    | Description                                                                      |
| --------| -------------------------------------------------------------------------------- |
| backend | Runs everything except the `api` container. Use this for working on `virtool`.   |
| ui      | Runs everything except the `ui` container. Use this for working on `virtool-ui`. |
