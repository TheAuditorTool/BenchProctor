# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest72210():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    return render_template_string(data)
