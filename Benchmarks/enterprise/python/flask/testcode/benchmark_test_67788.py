# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest67788():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    return Markup('<img src="' + str(data) + '">')
