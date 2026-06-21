# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest79857():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    return Markup('<div>' + str(data) + '</div>')
