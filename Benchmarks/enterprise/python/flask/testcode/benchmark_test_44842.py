# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest44842():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
