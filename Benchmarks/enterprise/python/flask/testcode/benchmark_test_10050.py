# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest10050():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
