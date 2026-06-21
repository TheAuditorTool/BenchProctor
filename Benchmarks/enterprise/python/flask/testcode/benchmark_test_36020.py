# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest36020():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
