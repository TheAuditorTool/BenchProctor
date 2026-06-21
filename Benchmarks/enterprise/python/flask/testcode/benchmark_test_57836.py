# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57836():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
