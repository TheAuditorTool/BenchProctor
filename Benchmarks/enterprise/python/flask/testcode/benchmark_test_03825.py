# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest03825():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    return render_template_string(data)
