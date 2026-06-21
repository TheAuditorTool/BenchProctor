# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest07722():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
