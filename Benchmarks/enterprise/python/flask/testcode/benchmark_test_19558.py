# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest19558():
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
