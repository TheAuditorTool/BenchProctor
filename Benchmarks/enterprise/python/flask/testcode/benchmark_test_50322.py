# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest50322():
    raw_body = request.get_data(as_text=True)
    os.remove(str(raw_body))
    return jsonify({"result": "success"})
