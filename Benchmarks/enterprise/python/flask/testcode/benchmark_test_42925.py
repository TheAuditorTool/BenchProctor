# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest42925():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = FormData(payload=config_value).payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
