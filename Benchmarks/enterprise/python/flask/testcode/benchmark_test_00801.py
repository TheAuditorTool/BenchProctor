# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00801():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    return render_template_string(data)
