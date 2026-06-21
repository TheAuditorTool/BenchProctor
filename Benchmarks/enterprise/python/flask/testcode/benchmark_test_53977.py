# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53977():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
