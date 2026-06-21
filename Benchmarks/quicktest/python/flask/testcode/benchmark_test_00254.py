# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest00254():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    return render_template_string(data)
