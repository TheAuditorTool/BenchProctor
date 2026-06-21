# SPDX-License-Identifier: Apache-2.0
import csv
import io
from flask import request, jsonify


def BenchmarkTest21139():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return jsonify({"result": "success"})
