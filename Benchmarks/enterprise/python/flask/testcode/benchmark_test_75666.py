# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest75666():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
