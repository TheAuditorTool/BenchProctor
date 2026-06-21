# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest72456():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    return Markup('<img src="' + str(data) + '">')
