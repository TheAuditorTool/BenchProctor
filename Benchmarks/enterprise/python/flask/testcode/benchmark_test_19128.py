# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest19128():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
