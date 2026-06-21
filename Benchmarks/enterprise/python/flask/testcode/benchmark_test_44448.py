# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest44448():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
