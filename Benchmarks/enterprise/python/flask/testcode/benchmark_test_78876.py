# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest78876():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    return Markup('<div>' + str(data) + '</div>')
