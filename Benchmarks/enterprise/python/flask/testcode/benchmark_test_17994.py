# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest17994():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    return render_template_string('{{ value }}', value=data)
