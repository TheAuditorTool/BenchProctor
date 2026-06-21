# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest10036():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    return render_template_string(data)
