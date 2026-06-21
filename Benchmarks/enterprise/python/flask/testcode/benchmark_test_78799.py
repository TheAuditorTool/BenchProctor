# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78799():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
