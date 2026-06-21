# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest22438():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    return render_template_string(data)
