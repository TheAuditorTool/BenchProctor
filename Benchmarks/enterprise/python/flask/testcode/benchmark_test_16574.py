# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest16574():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
