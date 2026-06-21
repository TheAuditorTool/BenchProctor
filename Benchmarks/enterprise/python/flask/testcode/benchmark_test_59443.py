# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest59443(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return render_template_string(data)
