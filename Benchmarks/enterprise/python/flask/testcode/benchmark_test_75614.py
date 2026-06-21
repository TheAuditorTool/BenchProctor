# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
import unicodedata


@dataclass
class FormData:
    payload: str

def BenchmarkTest75614():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
