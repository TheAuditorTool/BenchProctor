# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
import os


def BenchmarkTest15874():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
