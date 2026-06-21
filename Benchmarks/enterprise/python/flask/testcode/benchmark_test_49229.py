# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest49229():
    referer_value = request.headers.get('Referer', '')
    os.remove(str(referer_value))
    return jsonify({"result": "success"})
