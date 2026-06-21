# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest02686():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
