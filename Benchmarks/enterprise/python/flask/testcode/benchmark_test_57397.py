# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest57397():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
