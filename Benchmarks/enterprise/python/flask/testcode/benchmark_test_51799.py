# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest51799():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    return render_template_string(data)
