# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest07974():
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
