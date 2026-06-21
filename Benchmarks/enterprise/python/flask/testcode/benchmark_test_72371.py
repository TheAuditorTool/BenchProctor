# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest72371():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    return render_template_string('safe block: {{ value }}', value=data)
