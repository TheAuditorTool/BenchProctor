# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest52014(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
