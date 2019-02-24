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

# hello.feature: hello app features

Feature: Say Hello
    In order to save time on setup code for a problem
    As a developer
    I want a sample hello app written in Python3

    Scenario Outline: Only forename is given
        Given a shell executable app: "hello.py"
        When the app is executed with: "<args>"
        Then the app should print: "<message>"
        Examples: Args
            | args    | message |
            | Madonna | Hello Madonna! |
            | Prince  | Hello Prince!  |

    Scenario Outline: Both forename and surname are given
        Given a shell executable app: "hello.py"
        When the app is executed with: "<args>"
        Then the app should print: "<message>"
        Examples: Args
            | args            | message                |
            | Beyonce Knowles | Hello Beyonce Knowles! |
            | Jay Z           | Hello Jay Z!           |

    Scenario Outline: Excitement level can be specified
        Given a shell executable app: "hello.py"
        When the app is executed with: "<args>"
        Then the app should print: "<message>"
        Examples: Args
            | args                            | message                      |
            | Madonna         --excitement 10 | Hello Madonna!!!!!!!!!!      |
            | Beyonce Knowles --excitement  7 | Hello Beyonce Knowles!!!!!!! |
            | Jay Z           --excitement  3 | Hello Jay Z!!!               |
            | Prince          --excitement  1 | Hello Prince!                |

    Scenario: Message of the day file support
        Given a shell executable app: "hello.py"
        When the app is executed with: "Jesse Cook --motd motd"
        Then the app should print:
            """
            Hello Jesse Cook!
            P(A|B) = P(B|A) * P(A)
                     -------------
                         P(B)
            """
