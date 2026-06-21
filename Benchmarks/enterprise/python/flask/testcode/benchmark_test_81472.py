# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest81472():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
