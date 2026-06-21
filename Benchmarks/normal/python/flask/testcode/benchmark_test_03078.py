# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03078():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    return render_template_string(data)
