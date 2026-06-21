# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest12334():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
