# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest77900():
    field_value = request.form.get('field', '')
    os.system('echo ' + str(field_value))
    return jsonify({"result": "success"})
