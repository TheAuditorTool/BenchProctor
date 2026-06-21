# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest02421():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
