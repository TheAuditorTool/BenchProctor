# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest33302():
    xml_value = request.get_data(as_text=True)
    data = to_text(xml_value)
    return render_template_string('safe block: {{ value }}', value=data)
