# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00278():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})
