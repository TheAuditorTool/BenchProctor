# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest75177():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
