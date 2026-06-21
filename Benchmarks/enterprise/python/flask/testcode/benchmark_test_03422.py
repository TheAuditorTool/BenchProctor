# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03422():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    return render_template_string(data)
