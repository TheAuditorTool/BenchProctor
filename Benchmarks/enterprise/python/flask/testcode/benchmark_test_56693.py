# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os


def BenchmarkTest56693():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
