<br>

## Development Environment

<br>

### Remote Development

For this Python project/template, the remote development environment requires

* [Dockerfile](../.devcontainer/Dockerfile)
* [requirements.txt](../.devcontainer/requirements.txt)

An image is built via the command

```shell
docker build . --file .devcontainer/Dockerfile -t posteriors
```

On success, the output of

```shell
docker images
```

should include

<br>

| repository | tag    | image id | created  | size     |
|:-----------|:-------|:---------|:---------|:---------|
| posteriors | latest | $\ldots$ | $\ldots$ | $\ldots$ |


<br>

Subsequently, run a container, i.e., an instance, of the image `posteriors` via:

<br>

```shell
docker run --rm --gpus all --shm-size=16gb -i -t 
  -p 8000:8000 -p 8888:8888   
    -w /app --mount type=bind,src="$(pwd)",target=/app 
      -v ~/.aws:/root/.aws posteriors
```

<br>

Herein, `-p 8000:8000` maps the host port `8000` to container port `8000`.  Note, the container's working environment, i.e., -w, must be inline with this project's top directory.  In brief

* --rm: [automatically remove container](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the)
* -i: [interact](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di)
* -t: [tag](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your)
* -p: [publish a container's ports to its host](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s)

<br>

Get the name of the running instance of ``posteriors`` via:

```shell
docker ps --all
```

Never deploy a root container.  **Remember**, during the development phase the [container](../.devcontainer/Dockerfile) is a root container

> *... which can cause new files in mounted volumes to be created as the root user on your host machine.  To avoid this, run the container by specifying your user's userid:*
>
> $ docker run -u $(id -u):$(id -g) args...
>


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
