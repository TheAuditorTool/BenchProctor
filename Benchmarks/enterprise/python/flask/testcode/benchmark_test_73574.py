# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest73574():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
