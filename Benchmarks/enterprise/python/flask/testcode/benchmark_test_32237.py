# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify


def BenchmarkTest32237():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
