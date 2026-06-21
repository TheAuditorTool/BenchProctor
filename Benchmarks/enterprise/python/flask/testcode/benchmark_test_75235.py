# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def BenchmarkTest75235():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    return render_template_string('{{ value }}', value=data)
