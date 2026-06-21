# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest23124():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
