# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest07286():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
