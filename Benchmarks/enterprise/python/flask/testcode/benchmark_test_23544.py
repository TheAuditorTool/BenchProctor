# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import ast


def BenchmarkTest23544():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
