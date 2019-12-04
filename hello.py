#!venv/bin/python3
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

# hello.py: a sample hello app

from argcomplete import autocomplete
from argparse import ArgumentParser, ArgumentTypeError
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_request():
    return hello("Sammy", None, 1, None)


def hello(forename, surname, excitement, motd):
    msg = ""
    if surname:
        name = "%s %s" % (forename, surname)
    else:
        name = forename
    msg += "Hello %s" % name
    for i in range(excitement):
        msg += '!'
    msg += '\n'
    if motd:
        with open(motd, 'r') as f:
            msg += f.read()
    return msg


if __name__ == '__main__':
    def excitement(v):
        i = int(v)
        if i < 1 or i > 10:
            raise ArgumentTypeError("%s is not in the range [1-10]" % v)
        return i

    def motd(v):
        if not motd:
            return None
        try:
            with open(v, 'r'):
                pass
        except Exception as e:
            raise ArgumentTypeError("%s" % e)
        return v

    parser = ArgumentParser(description='hello')
    parser.add_argument('forename', type=str, help='Given name')
    parser.add_argument('surname', type=str, help='Family name', nargs='?')
    parser.add_argument('--excitement', type=excitement,
                        help='Your excitement level [1-10]', default=1)
    parser.add_argument('--motd', type=motd,
                        help='path to message of the day', default=None)
    autocomplete(parser)
    args = parser.parse_args()
    print(hello(args.forename,
                args.surname,
                args.excitement,
                args.motd), end='')
