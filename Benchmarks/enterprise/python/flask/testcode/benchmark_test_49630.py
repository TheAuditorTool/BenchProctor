# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest49630():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    return redirect(str(data))
