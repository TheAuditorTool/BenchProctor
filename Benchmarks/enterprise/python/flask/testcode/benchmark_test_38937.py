# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest38937(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    return render_template_string(data)
