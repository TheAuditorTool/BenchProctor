# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest15748():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    return Markup('<div>' + str(data) + '</div>')
