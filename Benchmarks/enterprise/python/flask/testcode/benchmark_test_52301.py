# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest52301():
    host_value = request.headers.get('Host', '')
    random.seed(int(host_value) if str(host_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
