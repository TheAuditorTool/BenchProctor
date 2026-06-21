# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest26769():
    raw_body = request.get_data(as_text=True)
    entries = os.listdir(str(raw_body))
    return jsonify({'listing': entries}), 200
