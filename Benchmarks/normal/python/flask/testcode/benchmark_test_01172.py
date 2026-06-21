# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest01172():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    return render_template_string(data)
