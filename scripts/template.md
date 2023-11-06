---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    notebook_metadata_filter: kernel
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
import pandas as pd
import requests
import json
```

```python
# load credentials
with open('../config.json') as f:
    config = json.load(f)
    data_path = config['data_path']
```
