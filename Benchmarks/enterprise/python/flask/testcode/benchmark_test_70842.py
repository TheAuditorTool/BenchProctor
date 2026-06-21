# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os


def BenchmarkTest70842():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
