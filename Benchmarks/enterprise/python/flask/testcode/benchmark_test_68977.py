# SPDX-License-Identifier: Apache-2.0
import os
from flask import redirect
import urllib.parse


def BenchmarkTest68977():
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
