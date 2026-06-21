# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest04676():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
