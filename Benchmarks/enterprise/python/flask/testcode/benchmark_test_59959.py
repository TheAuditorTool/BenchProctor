# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59959():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
