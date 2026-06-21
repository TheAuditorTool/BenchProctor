# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest18681():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
