# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import request, jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest80687():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
