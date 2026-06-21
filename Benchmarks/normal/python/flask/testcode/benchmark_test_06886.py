# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest06886():
    auth_header = request.headers.get('Authorization', '')
    random.seed(int(auth_header) if str(auth_header).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
