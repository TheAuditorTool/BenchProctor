# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest32715():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
