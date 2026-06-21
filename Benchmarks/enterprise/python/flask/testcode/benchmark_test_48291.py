# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest48291():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return render_template_string(data)
