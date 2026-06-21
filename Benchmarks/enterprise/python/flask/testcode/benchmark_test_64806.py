# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest64806():
    auth_header = request.headers.get('Authorization', '')
    random.seed(int(auth_header) if str(auth_header).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
