# Copyright 2019 Jesse J. Cook
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# steps.py: hello app step definitions

import os
from shutil import which
from subprocess import CalledProcessError, check_output
from behave import given, when, then


def is_rx(path):
    return (os.path.isfile(path)
            and os.access(path, os.R_OK)
            and os.access(path, os.X_OK)
            )


def is_read(path):
    return os.path.isfile(path) and os.access(path, os.R_OK)


def search_up(filename):
    path = '.'
    while(os.path.realpath(path) != '/'):
        rpath = os.path.realpath("%s/%s" % (path, filename))
        if is_rx(rpath):
            return rpath
        path = "../" + path
    return None


@given(u'a shell executable app: "{prog}"')
def step_given_a_shell_executable_app(context, prog):
    path = search_up(prog)
    assert path is not None
    context.program = path


@when(u'the app is executed with: "{args}"')
def step_when_the_app_is_executed_with(context, args):
    cmd = [which("python3"), context.program] + args.split()
    try:
        print(cmd)
        context.output = check_output(cmd)
    except CalledProcessError as e:
        context.output = e


@then(u'the app should print')
def step_then_the_app_should_print_text(context):
    assert context.output.decode(encoding='UTF-8').rstrip('\n') == context.text


@then(u'the app should print: "{output}"')
def step_then_the_app_should_print_output(context, output):
    assert context.output.decode(encoding='UTF-8').rstrip('\n') == output
