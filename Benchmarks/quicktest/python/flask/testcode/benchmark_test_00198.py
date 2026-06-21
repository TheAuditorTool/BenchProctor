# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest00198():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    return Markup('<div>' + str(data) + '</div>')
