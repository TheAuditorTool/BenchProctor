# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00481():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
