# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
import os


def BenchmarkTest28337():
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
