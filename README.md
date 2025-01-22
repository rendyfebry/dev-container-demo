# Demo App to showcase Dev Container

## What are Development Containers?

A development container (or dev container for short) allows you to use a container as a full-featured development environment. It can be used to run an application, to separate tools, libraries, or runtimes needed for working with a codebase, and to aid in continuous integration and testing. Dev containers can be run locally or remotely, in a private or public cloud, in a variety of supporting tools and editors.

## Pre-requisites
* Visual Studio Code
* Docker
* Python

## Development

### Run the app locally
1. Setup virtual environment
```bash
python3 -m venv .venv
```

2. Activate virtual environment
```bash
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the app
```bash
uvicorn app.main:app --reload --port 8181
```
