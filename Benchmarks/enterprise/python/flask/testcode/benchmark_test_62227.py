# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest62227():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
