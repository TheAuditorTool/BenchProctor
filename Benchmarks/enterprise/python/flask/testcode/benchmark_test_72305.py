# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest72305():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    json.loads(data)
    return jsonify({"result": "success"})
