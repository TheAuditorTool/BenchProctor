# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest26286():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
