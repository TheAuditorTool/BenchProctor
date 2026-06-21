# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest34361():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    os.remove(str(data))
    return jsonify({"result": "success"})
