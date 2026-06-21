# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32951():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})
