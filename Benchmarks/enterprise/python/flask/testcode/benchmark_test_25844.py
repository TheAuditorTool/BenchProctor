# SPDX-License-Identifier: Apache-2.0
import csv
import io
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest25844():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return jsonify({"result": "success"})
