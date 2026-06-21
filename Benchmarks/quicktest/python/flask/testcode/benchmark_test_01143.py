# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest01143():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
