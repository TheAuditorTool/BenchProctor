# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest05895():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    return render_template_string(data)
