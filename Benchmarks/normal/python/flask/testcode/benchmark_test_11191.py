# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest11191():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
