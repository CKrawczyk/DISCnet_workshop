# DISCnet_workshop
DISCnet workshop repository

## Install

### make a clean python env (optional)
If using conda:

```bash
conda create --name discnet_env python=3.10
conda activate discnet_env
```

If using venv

```bash
python3 -m venv discnet_env
source discnet_env/bin/activate
```

### pip install locally in "edit" mode

```bash
pip install -e .[dev]
```

## run tests
To run tests use
```bash
pytest
```

To run with coverage use
```bash
coverage run -m pytest
coverage report
```
