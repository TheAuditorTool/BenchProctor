# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest04681():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    return redirect(str(data))
