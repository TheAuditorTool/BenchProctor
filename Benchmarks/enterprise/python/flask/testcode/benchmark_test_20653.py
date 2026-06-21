# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest20653():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return render_template_string(data)
