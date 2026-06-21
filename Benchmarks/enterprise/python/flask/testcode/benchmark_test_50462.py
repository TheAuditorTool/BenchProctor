# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest50462():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
