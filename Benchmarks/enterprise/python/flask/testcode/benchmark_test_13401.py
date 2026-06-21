# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest13401():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
