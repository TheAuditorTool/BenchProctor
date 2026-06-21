# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest56151():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    return render_template_string(data)
