# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest19229():
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
