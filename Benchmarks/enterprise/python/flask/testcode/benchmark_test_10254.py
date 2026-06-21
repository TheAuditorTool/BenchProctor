# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest10254():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    return Markup('<img src="' + str(data) + '">')
