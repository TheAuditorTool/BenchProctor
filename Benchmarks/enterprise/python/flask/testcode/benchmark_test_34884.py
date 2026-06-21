# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest34884():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
