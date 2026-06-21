# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest13683():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
