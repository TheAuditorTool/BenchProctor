# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest00467():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    return Markup('<div>' + str(data) + '</div>')
