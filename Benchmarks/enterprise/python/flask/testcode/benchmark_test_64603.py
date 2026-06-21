# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64603():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return jsonify({"result": "success"})
