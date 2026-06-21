# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest79982():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
