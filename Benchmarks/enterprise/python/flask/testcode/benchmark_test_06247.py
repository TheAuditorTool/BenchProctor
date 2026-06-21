# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest06247():
    user_id = request.args.get('id', '')
    if re.search('[a-zA-Z0-9_-]+', str(user_id)):
        return jsonify({'validated': str(user_id)}), 200
    return jsonify({"result": "success"})
