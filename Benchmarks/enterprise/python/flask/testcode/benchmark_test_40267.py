# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest40267():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
