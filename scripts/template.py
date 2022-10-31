# %%
import pandas as pd
import requests
import json

# %%
# load credentials
with open('../config.json') as f:
    config = json.load(f)
    data_path = config['data_path']
