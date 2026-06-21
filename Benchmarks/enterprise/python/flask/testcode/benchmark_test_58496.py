# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest58496():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
