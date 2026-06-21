# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest09659():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = FormData(payload=json_value).payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
