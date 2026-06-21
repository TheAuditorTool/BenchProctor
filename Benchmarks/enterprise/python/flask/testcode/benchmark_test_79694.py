# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest79694():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
