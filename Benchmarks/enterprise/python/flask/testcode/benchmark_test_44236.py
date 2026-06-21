# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest44236():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
