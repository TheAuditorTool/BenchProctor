# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def BenchmarkTest37906():
    auth_header = request.headers.get('Authorization', '')
    if re.search('[a-zA-Z0-9_-]+', str(auth_header)):
        return jsonify({'validated': str(auth_header)}), 200
    return jsonify({"result": "success"})
