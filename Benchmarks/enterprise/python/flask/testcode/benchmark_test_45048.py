# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest45048():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
