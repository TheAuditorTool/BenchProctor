# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest19177():
    field_value = request.form.get('field', '')
    with open('/var/uploads/' + str(field_value), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
