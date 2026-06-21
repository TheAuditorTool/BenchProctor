# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os


def BenchmarkTest02523():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
