# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77764():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return jsonify({"result": "success"})
