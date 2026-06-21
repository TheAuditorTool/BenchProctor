# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest02719():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    return redirect(str(data))
