# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest65391():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return render_template_string(data)
