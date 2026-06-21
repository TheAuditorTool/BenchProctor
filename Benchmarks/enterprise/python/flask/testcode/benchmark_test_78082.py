# SPDX-License-Identifier: Apache-2.0
import random
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest78082():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
