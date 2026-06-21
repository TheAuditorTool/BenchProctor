# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest12596():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ns = SimpleNamespace(payload=config_value)
    data = getattr(ns, 'payload')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
