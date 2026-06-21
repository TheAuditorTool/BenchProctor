# SPDX-License-Identifier: Apache-2.0
import yaml
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest47993():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
