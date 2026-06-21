# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest69947():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return Markup('<img src="' + str(data) + '">')
