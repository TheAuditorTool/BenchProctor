# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest75310():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    return render_template_string(data)
