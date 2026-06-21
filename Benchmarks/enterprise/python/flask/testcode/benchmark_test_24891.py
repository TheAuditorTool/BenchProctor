# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest24891():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
