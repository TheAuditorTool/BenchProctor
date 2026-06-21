# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest18968():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
