# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest31418():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
