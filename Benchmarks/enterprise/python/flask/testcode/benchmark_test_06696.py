# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest06696():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    return render_template_string(data)
