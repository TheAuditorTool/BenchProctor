# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest21129():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    return redirect(str(data))
