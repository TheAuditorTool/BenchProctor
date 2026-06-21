# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest53067():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
