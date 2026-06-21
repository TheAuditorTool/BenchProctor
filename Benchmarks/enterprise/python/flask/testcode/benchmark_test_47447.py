# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest47447():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
