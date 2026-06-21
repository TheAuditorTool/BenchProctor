# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest07672():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
