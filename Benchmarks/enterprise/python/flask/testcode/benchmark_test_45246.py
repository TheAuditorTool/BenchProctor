# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
import os


def BenchmarkTest45246():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
