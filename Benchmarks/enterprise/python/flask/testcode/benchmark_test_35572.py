# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest35572():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
