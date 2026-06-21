# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest40641():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    return render_template_string(data)
