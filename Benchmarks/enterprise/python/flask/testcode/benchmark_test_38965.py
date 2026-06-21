# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import os


def BenchmarkTest38965():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return redirect(str(data))
