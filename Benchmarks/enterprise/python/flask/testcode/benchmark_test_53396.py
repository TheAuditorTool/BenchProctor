# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest53396():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
