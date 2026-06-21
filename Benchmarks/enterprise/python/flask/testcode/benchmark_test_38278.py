# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest38278():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
