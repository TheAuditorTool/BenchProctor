# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest12431():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
