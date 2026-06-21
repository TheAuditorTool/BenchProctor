# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest24257():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    return render_template_string(data)
