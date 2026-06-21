# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00519():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    return render_template_string('{{ value }}', value=data)
