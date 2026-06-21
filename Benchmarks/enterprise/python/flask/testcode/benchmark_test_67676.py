# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest67676():
    xml_value = request.get_data(as_text=True)
    data = RequestPayload(xml_value).value
    return render_template_string(data)
