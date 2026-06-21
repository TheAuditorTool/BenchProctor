# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest22685():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    return Markup('<div>' + str(data) + '</div>')
