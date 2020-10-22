# Transmission Helper

## Setup

## Docker

Build Webserver

```bash
docker build . -f transmission_helper_webserver/Dockerfile --tag transmission_helper_webserver:latest
```

Build Scheduler

```bash
docker build . -f transmission_helper_scheduler/Dockerfile --tag transmission_helper_scheduler:latest
```

Run Webserver

```bash
docker run --name transmission_helper_webserver -p 5000:5000 --rm transmission_helper_webserver:latest
```

Run Scheduler

```bash
docker run --name transmission_helper_scheduler --rm transmission_helper_scheduler:latest
```
