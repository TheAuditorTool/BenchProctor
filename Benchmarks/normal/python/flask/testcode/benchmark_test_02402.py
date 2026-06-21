# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest02402():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
