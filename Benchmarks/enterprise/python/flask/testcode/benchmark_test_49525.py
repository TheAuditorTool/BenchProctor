# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest49525():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
