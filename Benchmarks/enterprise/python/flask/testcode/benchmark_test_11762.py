# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest11762():
    referer_value = request.headers.get('Referer', '')
    random.seed(int(referer_value) if str(referer_value).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
