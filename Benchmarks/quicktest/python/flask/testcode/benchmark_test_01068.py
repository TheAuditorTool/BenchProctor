# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01068():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    return render_template_string(data)
