# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest79881():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    return Markup('<div>' + str(data) + '</div>')
