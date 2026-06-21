# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest68375():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
