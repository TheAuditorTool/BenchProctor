# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest59700():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    return Markup('<div>' + str(data) + '</div>')
