# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest17230():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
