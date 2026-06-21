# SPDX-License-Identifier: Apache-2.0
import csv
import io
from flask import request, jsonify


def BenchmarkTest69847():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return jsonify({"result": "success"})
