# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11524():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})
