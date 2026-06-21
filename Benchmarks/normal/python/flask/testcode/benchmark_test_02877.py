# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest02877():
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    return render_template_string(data)
