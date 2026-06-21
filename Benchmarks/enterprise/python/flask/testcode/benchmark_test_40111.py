# SPDX-License-Identifier: Apache-2.0
import csv
import io
from flask import request, jsonify


def BenchmarkTest40111():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return jsonify({"result": "success"})
