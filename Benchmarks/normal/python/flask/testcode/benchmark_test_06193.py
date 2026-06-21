# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest06193():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    os.remove(str(data))
    return jsonify({"result": "success"})
