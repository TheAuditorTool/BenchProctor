# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest69163():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    os.remove(str(data))
    return jsonify({"result": "success"})
