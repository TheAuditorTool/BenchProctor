# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest47599():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    return render_template_string(data)
