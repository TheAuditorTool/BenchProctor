# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09490():
    raw_body = request.get_data(as_text=True)
    os.system('echo ' + str(raw_body))
    return jsonify({"result": "success"})
