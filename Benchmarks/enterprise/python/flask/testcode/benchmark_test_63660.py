# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest63660():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
