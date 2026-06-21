# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest28468():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
