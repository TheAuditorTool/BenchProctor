# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request
from flask import redirect
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest42394():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
