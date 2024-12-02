# Jupyter Project Template

This repository is a project template for a jupyter notebook runnable via [Visual Studio Code's Dev Containers feature](https://code.visualstudio.com/docs/devcontainers/containers).

## Running Locally

Clone this repository directly or create a repo from [GitHub's repository template feature](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

Create a local copy of the environment variables file:

```
cp .env.example .env
```

and modify the values to your heart's content. These values can be made available within the containers specified in `docker-compose.yml`.

From there, you can run the containers via `docker compose` directly:

```
docker compose up
```

or by opening the repository in VS Code with the Dev Containers extension and running the command: *Rebuild and Reopen in Container*.
