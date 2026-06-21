# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14888():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    return render_template_string('{{ value }}', value=data)
