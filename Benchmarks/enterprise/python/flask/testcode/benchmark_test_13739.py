# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13739():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
