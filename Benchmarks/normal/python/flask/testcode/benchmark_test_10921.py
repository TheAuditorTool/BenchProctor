# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest10921():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
