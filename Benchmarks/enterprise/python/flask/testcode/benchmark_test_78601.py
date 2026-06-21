# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest78601(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return render_template_string('safe block: {{ value }}', value=data)
