# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest38065():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
