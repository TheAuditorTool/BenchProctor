# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest34183():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
