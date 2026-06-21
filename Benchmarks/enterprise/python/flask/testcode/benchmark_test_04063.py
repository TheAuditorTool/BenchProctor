# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest04063():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
