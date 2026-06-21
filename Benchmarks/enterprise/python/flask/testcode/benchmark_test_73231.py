# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest73231():
    field_value = request.form.get('field', '')
    if field_value not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = field_value
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
