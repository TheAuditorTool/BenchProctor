# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest02178():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    return render_template_string(data)
