# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest56117():
    multipart_value = request.form.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
