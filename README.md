
## RI projects template

This template is the basis for (standard) RI projects. 
It provides an environment to set up **JupyterLab** with **Jupytext** for better version control.

The repository has only one subfolder (/scripts) that contains notebooks rendered with Jupytext.\
*(see below for instructions on how to use the notebooks)*

use the following command to create all notebooks from scripts at once:
```
jupytext --sync scripts/*
```

### environment.yml

- conda environment with essential libraries
- can be used as a "global" environment because most of the libraries are reused across projects

install and activate the environment
```
conda env create --file environment.yml
conda activate ri
```
after use
```
conda deactivate ri
```
https://docs.conda.io/en/latest/miniconda.html

### jupytext.toml

configures Jupytext (used for better version control of notebooks)

- /scripts contains plain text notebooks (metadata has been removed)
- when opened as a notebook (in JupyterLab), Jupytext creates an .ipynb file under /notebooks
- this notebook can be run and modified and when saved, the plain text notebook under /scripts is modified (and metadata stripped)
- the notebooks themselves are gitignored

https://jupytext.readthedocs.io/en/latest/index.html

### configTEMPLATE.json
- contains credentials, e.g. api keys or path to data
- path to data can be local, but ideally it is shared with the team (sharepoint)
- make sure to remove the substring TEMPLATE in a local repository
