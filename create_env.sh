# venv.sh
#!/usr/bin/env

export python_ver=3.11
pyenv install ${python_ver}
pyenv virtualenv ${python_ver} dlgo
