# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest41315():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    kind = 'json' if str(config_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = config_value
            data = parsed
        case _:
            data = config_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
