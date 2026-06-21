# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest81065():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    return redirect(str(data))
