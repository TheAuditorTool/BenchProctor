# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest36130():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
