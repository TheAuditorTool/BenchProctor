# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest00706():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return render_template_string(data)
