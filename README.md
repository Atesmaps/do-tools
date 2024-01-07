# Digital Ocean Tools - Atesmaps

Project with DigitalOcean Tools that are used to
maintain Atesmaps infrastructure.

## Deploy

This project uses GitHub Actions for manage deployments.
See [deploy.yaml](.github/workflows/deploy.yaml) for more details.

## Usage

### Docker

```bash
docker run --rm atesmaps-do-tools:latest {do-tool-action}
```

Run `-h` to display help usage:

```bash
docker run --rm atesmaps-do-tools:latest -h
```

#### Example

- Action `volume-snapshots`:
    ```bash
    docker run \
      --rm \
      --name atesmaps-do-tools \
      atesmaps-do-tools:latest \
      volume-snapshots \
      --volume-ids abcdefghi-0000-00xx-000x-000000xxxxxx \
      --retention-days 10
    ```

### Python3

First of all you need to activate `pipenv shell`:
```bash
pip install pipenv && pipenv shell
```

Run `do-tools` action:
```bash
python3 src/main.py {do-tool-action}
```

Run `-h` to display help usage:
```bash
python3 src/main.py -h
```

## Local Development

This project requires `Python3`.

#### Steps

1. Install `pipenv`:
    ```bash
    pip install --upgrade pip && pip install pipenv
    ```
2. Activate virtualenv:
    ```bash
    pipenv shell
    ```
3. Run Python script:
    ```bash
    python3 src/main.py
    ```

## Collaborators
- Nil Torrano: <ntorrano@atesmaps.org>
- Atesmaps: <info@atesmaps.org>
