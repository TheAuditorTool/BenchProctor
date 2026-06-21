# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest28604():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    return Markup('<div>' + str(data) + '</div>')
