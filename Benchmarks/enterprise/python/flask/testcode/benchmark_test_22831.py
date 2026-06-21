# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest22831():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = FormData(payload=json_value).payload
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
