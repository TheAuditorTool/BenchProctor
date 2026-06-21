# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def BenchmarkTest79514():
    env_value = os.environ.get('USER_INPUT', '')
    return Markup('<div>' + str(env_value) + '</div>')
