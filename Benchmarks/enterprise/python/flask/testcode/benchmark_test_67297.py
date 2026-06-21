# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest67297():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
