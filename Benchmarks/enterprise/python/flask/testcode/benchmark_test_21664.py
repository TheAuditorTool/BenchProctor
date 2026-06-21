# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest21664():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
