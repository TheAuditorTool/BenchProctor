# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest25589():
    multipart_value = request.form.get('multipart_field', '')
    with open('/var/uploads/' + str(multipart_value), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
