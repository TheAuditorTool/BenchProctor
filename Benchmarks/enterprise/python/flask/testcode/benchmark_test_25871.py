# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest25871():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
