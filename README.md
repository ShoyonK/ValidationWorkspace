# CI/CD Pipeline

This repository includes a CI/CD pipeline using GitHub Actions and dependency management via astral uv. The pipeline ensures code quality in accordance to PEP, runs tests, and keeps the workspace clean.

## CI/CD Pipeline Overview

The GitHub Actions workflow is defined in `.github/workflows/ci-cd.yml`. It runs automatically on:
- **Push events** on any branch
- **Pull requests** to any branch

### Pipeline Stages
1. Checkout Repository – Fetches the latest code.
2. Setup Python – Installs Python 3.12.
3. Install Dependencies – Uses `uv` to manage dependencies via `uv.lock`.
4. Run Ruff Linter – Ensures code follows PEP8 and best practices.
5. Run Unit Tests – Executes `pytest` and saves test logs.
6. Upload Test Logs as Artifact – Saves test results for reference.
7. Clean Workspace – Removes temporary files to keep the environment clean.

---

## `uv` Usage in the Pipeline

[`uv`](https://github.com/astral-sh/uv) is used for fast dependency management. It creates a virtual environment and syncs dependencies efficiently.

### Installing `uv` and Setting Up Dependencies
In the CI/CD workflow, dependencies are installed using:
  ```sh
  python3 -m pip install --upgrade pip
  pip install uv
  uv venv .venv
  source .venv/bin/activate
  uv pip sync uv.lock
  ```
This ensures that the exact package versions from `uv.lock` are installed.

### **Generating `uv.lock` for Local Development
To generate a `uv.lock` file from `pyproject.toml`, run:
```sh
uv pip compile pyproject.toml --output uv.lock
```
This locks dependencies to specific versions.

### Installing Dependencies Locally
To sync dependencies from `uv.lock`, run:
```sh
uv pip sync uv.lock
```
This installs the same package versions as in the CI/CD environment.

### Updating Dependencies
To update dependencies and regenerate `uv.lock`:
```sh
uv pip compile --upgrade
```
Then, commit the updated `uv.lock` file.

---

## Running the Pipeline Locally
You can manually run the steps from the CI/CD pipeline on your machine:
```sh
source .venv/bin/activate
ruff check .  # Run linter
pytest  # Run tests
```

---

## Troubleshooting
### `uv.lock` Not Being Created
If `uv.lock` is missing after running `uv pip compile`, ensure:
- `pyproject.toml` contains a `[project.dependencies]` section.
- Run `uv pip compile pyproject.toml --output uv.lock` explicitly.

