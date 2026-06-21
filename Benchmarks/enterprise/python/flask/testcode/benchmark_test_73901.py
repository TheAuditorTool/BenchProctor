# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest73901():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    return redirect(str(data))
