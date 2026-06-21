# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from urllib.parse import unquote
from flask import request


def BenchmarkTest75563():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    return render_template_string(data)
