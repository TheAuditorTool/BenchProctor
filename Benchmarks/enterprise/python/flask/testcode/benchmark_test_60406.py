# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest60406():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
