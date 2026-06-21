# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00100():
    field_value = request.form.get('field', '')
    os.chmod('/var/app/data/' + str(field_value), 0o777)
    return jsonify({"result": "success"})
