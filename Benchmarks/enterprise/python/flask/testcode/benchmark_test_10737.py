# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest10737():
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    return str(data), 200, {'Content-Type': 'text/html'}
