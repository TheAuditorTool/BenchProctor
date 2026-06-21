# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest22742():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
