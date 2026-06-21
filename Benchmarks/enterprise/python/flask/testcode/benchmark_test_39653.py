# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest39653():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
