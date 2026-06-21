# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest22292():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    pending = list(str(config_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    auth_check('user', data)
    return jsonify({"result": "success"})
