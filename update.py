import json
from copy import deepcopy
from pprint import pprint
from typing import Dict
from semver import VersionInfo
import requests
import yaml


BASE_URL = "https://hub.docker.com/v2/repositories"

ORGANIZATION = "virtool"

REPOSITORIES = (
    "build-index",
    "create-sample",
    "create-subtraction",
    "migration",
    "nuvs",
    "pathoscope",
    "virtool",
    "ui",
)


def load_tags_from_json():
    with open(".tags", "r") as f:
        return json.load(f)


def get_tags():
    tags = {}

    for repo in REPOSITORIES:
        body = requests.get(f"{BASE_URL}/{ORGANIZATION}/{repo}/tags")
        data = body.json()

        tags[f"{ORGANIZATION}/{repo}"] = data["results"][0]["name"]

    with open(".tags", "w") as f:
        json.dump(tags, f)

    return tags


def update_yaml(tags: Dict[str, str]):
    with open("docker-compose.yml") as f:
        data = yaml.safe_load(f)

    updated = deepcopy(data)

    for service_name, service in data["services"].items():
        if service_name == "api" or service_name == "jobs-api":
            continue

        name, version = service["image"].split(":")

        if name in tags:
            yaml_ver = VersionInfo.parse(version)
            repo_ver = VersionInfo.parse(tags[name])

            if repo_ver > yaml_ver:
                _, bare_name = name.split("/")
                updated["services"][bare_name]["image"] = f"{name}:{version}"

    for service_name in ("api", "jobs-api"):
        version = tags["virtool/virtool"]

        if service_name in updated["services"]:
            updated["services"][service_name]["image"] = f"virtool/virtool:{version}"

    with open("docker-compose.yml", "w") as f:
        yaml.dump(updated, f, default_flow_style=False, width=1000)


if __name__ == "__main__":
    update_yaml(get_tags())


