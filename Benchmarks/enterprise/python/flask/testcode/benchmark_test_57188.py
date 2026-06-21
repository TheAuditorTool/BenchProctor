# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest57188():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
