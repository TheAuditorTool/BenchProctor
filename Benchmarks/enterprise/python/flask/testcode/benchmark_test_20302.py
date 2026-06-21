# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest20302():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    yaml.safe_load(data)
    return jsonify({"result": "success"})
