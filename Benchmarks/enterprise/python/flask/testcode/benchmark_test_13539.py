# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest13539():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
