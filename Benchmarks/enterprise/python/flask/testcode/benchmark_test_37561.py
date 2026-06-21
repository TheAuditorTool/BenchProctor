# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest37561():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    return render_template_string(data)
