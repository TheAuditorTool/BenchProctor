# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest72901():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    return Markup('<div>' + str(data) + '</div>')
