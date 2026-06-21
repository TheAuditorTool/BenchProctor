# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest02844():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    return render_template_string(data)
