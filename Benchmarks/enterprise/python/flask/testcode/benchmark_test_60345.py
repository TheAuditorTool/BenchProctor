# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest60345():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
