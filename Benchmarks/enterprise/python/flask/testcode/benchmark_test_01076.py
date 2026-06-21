# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest01076():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    os.remove(str(data))
    return jsonify({"result": "success"})
