# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest58915():
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
