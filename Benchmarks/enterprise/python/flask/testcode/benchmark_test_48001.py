# SPDX-License-Identifier: Apache-2.0
import random
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest48001():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
