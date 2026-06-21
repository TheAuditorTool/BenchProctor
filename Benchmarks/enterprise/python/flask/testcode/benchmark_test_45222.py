# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest45222():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
