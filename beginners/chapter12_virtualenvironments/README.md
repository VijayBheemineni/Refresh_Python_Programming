# Chapter 12: Virtual Environments and Packages

This chapter covers creating and managing virtual environments, installing packages with pip, and managing project dependencies.

# Virtual Environments 

## Why Virtual environments
- Python applications will use packages and modules that don't come as part of standard library. Different applications require different packages and different versions of same package. So we can solve this issue by creating 'virtual environment'.
- Generally for each application we create 'virtual environment' and install require packages and modules.

## Creating virtual environment
- Module used to create and manage virtual environments is called `venv`. 

### Create virtual environment
- Below we are creating virtual environment called '.venv/vijay_sagemaker'. This creates new directory '.venv/vijay_sagemaker' in current directory.
```
python -m venv .venv/vijay_sagemaker
```
- Activate the environment. Now we have new python environment. Packages installed this environment only belong to this environment.
```
source .venv/vijay_sagemaker/bin/activate
```
- Check current packages
```
pip list  
Package Version
------- -------
pip     25.3
```
- Install packages
```
 pip install cowsay

>>> import cowsay
>>> cowsay.cow("Learning AI")
  ___________
| Learning AI |
  ===========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||
>>> exit
```
- Check installed packages
```
pip list
Package Version
------- -------
cowsay  6.1
pip     25.3
```
- Deactivate Python virtual environment
```
deactivate
```

# Managing Packages with pip
- 'pip'(PIP installs packages). It will install packages from https://pypi.org/

## Install packages
```
 pip install cowsay
```
- Show information about packages
```
pip show cowsay
```
- List all packages installed
```
pip list
```
- `pip freeze` allows us to save list of packages installed in current environment.
```
pip freeze > requirements.txt
```
- Install packages from `requirements.txt`
```
pip install -r requirements.txt
```