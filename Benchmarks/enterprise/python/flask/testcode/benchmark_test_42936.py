# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest42936():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
