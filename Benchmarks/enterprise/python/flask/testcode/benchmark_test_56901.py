# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest56901():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    return Markup('<div>' + str(data) + '</div>')
