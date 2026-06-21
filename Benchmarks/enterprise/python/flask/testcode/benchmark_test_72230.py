# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest72230():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    return str(data), 200, {'Content-Type': 'text/html'}
