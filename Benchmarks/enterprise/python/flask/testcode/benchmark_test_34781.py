# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest34781():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
