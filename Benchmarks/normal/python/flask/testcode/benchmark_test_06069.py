# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest06069():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
