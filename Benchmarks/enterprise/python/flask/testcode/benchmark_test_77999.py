# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest77999():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})
