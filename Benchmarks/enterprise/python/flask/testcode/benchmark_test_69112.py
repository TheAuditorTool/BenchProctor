# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest69112():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
