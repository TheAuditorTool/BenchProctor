# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04219():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    os.remove(str(data))
    return jsonify({"result": "success"})
