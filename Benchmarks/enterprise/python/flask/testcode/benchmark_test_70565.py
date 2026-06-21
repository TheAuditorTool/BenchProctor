# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest70565():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
