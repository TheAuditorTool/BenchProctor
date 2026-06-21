# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest67355():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    return redirect(str(data))
