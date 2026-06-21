# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest15287():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
