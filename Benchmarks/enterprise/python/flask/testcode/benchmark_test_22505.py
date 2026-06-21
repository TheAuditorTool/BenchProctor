# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest22505():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
