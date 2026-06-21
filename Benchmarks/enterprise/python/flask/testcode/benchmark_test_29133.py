# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest29133():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
