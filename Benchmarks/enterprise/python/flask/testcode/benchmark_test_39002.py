# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import tempfile


@dataclass
class FormData:
    payload: str

def BenchmarkTest39002():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
