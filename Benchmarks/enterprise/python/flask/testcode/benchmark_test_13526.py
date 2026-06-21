# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest13526():
    referer_value = request.headers.get('Referer', '')
    yaml.safe_load(referer_value)
    return jsonify({"result": "success"})
