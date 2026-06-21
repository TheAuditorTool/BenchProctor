# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest63777():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    return Markup('<div>' + str(data) + '</div>')
