# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest02258():
    upload_name = request.files['upload'].filename
    return Markup('<img src="' + str(upload_name) + '">')
