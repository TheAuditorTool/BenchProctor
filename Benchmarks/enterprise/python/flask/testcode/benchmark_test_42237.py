# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def BenchmarkTest42237():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    return render_template_string('{{ value }}', value=data)
