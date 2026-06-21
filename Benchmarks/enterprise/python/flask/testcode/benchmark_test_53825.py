# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest53825():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    return render_template_string(data)
