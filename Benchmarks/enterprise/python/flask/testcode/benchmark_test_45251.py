# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest45251():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
