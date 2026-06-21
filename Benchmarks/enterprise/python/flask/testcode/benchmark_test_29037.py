# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest29037():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    return Markup('<div>' + str(data) + '</div>')
