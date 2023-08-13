# Overview

```
docker pull --platform=linux/amd64 gurobi/python
```
```
#!/bin/bash

read -p "Choose a docker image #: " num

case "$num" in
        1) name="continuumio/miniconda3"
        ;;
        2) name="gurobi/python"
esac

echo $name

docker run -it -d -v /Users/tim/Documents/Programming:/root --platform=linux/amd64 $name

# docker run -it -d -v $(pwd):/root $name
```
[https://hub.docker.com/r/gurobi/python](https://hub.docker.com/r/gurobi/python) (vscode ver_1.18.0)\
[https://phoenixnap.com/kb/how-to-commit-changes-to-docker-image](https://phoenixnap.com/kb/how-to-commit-changes-to-docker-image)\
(After installing docker desktop, don't move its directory, or it'll fail to be recongnized)
