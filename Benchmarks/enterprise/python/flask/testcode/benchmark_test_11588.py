# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest11588():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
