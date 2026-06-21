# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest21203():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    return render_template_string(data)
