# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest32502():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    return Markup('<div>' + str(data) + '</div>')
