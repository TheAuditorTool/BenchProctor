# SPDX-License-Identifier: Apache-2.0
import csv
import io
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest14492():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = FormData(payload=json_value).payload
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return jsonify({"result": "success"})
