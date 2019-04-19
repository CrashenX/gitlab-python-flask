# hello

hello app

## Getting Started

1. Setup virtual environment

        python3 -m venv venv
        venv/bin/pip install -U pip
        venv/bin/pip install -r requirements.txt
        venv/bin/pip install -r test-requirements.txt

2. Running the tests

        venv/bin/tox

3. Usage

        ./hello.py -h


### Gitlab Configuration

Make sure you set the CI/CD env variable in the GitLab webui:

    KUBE_INGRESS_BASE_DOMAIN: <your.base.domain.com>

### (Optional) Tab Completion

Docs: https://argcomplete.readthedocs.io/en/latest/index.html

    venv/bin/register-python-argcomplete hello.py>~/.bash_completion.d/hello.sh
    complete | grep hello.py  # if you see: complete -F _minimal ./hello.py
    complete -r ./hello.py    # then run this to remove
    source ~/.bash_completion.d/hello.sh
    complete | grep hello.py  # should see: complete -o default -o nospace -F _python_argcomplete hello.py

NB: You might need to create `~/.bash_completion` and source in `~/.bashrc`

    for bcfile in ~/.bash_completion.d/* ; do
        [ -f "$bcfile" ] && . $bcfile
    done
