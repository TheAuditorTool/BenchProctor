# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest31544():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
