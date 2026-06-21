# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest80165():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
