# Python Flask GitLab Template

A simple hello flask app configured to run on GitLab.

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

The `.gitlab-ci.yml` in this repo is derived from GitLab's Auto DevOps
Template. It is tweaked to deploy apps on the same cluster that GitLab
is running. It leverages the nginx-ingress-controller and cert-manager
(with both a staging and production cluster-issuer) as GitLab. If
it does not work out of the box for you, the first place to look
would be at the following variables in `.gitlab-ci.yml`:

- `HELM_UPGRADE_EXTRA_ARGS`
- `HTTPS_PORT`

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
