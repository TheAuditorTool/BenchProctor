# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest03437():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    return Markup('<div>' + str(data) + '</div>')
