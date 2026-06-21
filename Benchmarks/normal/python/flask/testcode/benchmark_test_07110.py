# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07110():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    return render_template_string(data)
