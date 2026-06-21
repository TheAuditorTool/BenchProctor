# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest52150():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
