# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest39372():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    return render_template_string(data)
