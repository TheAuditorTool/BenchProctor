# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest00135():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    return render_template_string(data)
