import sys
import os
import json
import datetime
import yaml


def update_package_json(version):
    with open("package.json", "r+") as f:
        data = json.load(f)
        data["version"] = version
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()


def update_gradle_version(version):
    with open("gradle.properties", "r+") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.strip().startswith("version"):
                lines[i] = f'version = "{version}"\n'
                break
        f.seek(0)
        f.writelines(lines)
        f.truncate()


def update_helm_chart_version(version):
    with open("../chart/Chart.yaml", "r+") as f:
        data = yaml.safe_load(f)
        data["version"] = version
        data["appVersion"] = version
        f.seek(0)
        yaml.dump(data, f, default_flow_style=False)
        f.truncate()


def main():
    if len(sys.argv) < 3:
        print("Usage: python update_version.py <release_type> <version> <targets>")
        print("Targets: comma-separated list of targets to update (package,json,gradle,helm)")
        sys.exit(1)

    release_type = sys.argv[1]
    version = sys.argv[2]
    version.split(".")
    major = version[0]
    minor = version[2]
    patch = version[4]
    print(f"Release type: {release_type}")
    print(f"Version: {version}")
    print(f"Major: {major}")
    print(f"Minor: {minor}")
    print(f"Patch: {patch}")
    if release_type == "releaseCandidate":
        release_candidate_version = version[3]
    targets = sys.argv[3].split(",")

    if release_type == "develop":
        now = datetime.datetime.now()
        build_number = int(now.timestamp())
        version = f"{major}.{minor}.0.{build_number}"
    elif release_type == "releaseCandidate":
        version = f"{major}.{minor}.0.RC{int(release_candidate_version)+1}"
    elif release_type == "release":
        version = f"{major}.{int(minor)+1}.0"
    elif release_type == "hotfix":
        version = f"{major}.{minor}.{int(patch)+1}"
    else: 
        print("Invalid release type")
        sys.exit(1)

    if "package.json" in targets:
        update_package_json(version)
    if "gradle" in targets:
        update_gradle_version(version)
    if "helm" in targets:
        update_helm_chart_version(version)

    print(f"Updated versions to: {version} in targets: {', '.join(targets)}")


if __name__ == "__main__":
    main()
