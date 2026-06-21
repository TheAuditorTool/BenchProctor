# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest45005():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
