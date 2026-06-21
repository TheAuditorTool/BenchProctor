# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest13471():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return Markup('<div>' + str(data) + '</div>')
