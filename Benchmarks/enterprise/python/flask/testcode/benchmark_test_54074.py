# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os


def BenchmarkTest54074():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    return Markup('<div>' + str(data) + '</div>')
