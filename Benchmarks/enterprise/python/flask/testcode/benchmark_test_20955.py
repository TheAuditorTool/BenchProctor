# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest20955():
    upload_name = request.files['upload'].filename
    return Markup('<div>' + str(upload_name) + '</div>')
