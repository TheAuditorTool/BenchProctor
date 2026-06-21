# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest64016():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
