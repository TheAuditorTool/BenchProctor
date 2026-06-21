# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09804():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    reader = make_reader(config_value)
    data = reader()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
