# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest28281():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
