# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest45588():
    referer_value = request.headers.get('Referer', '')
    random.seed(int(referer_value) if str(referer_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
