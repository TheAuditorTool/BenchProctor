# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest07391():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    random.seed(int(forwarded_ip) if str(forwarded_ip).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
