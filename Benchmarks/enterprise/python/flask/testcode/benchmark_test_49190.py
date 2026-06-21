# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest49190():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    return Markup('<img src="' + str(data) + '">')
