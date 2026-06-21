# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from urllib.parse import unquote
from flask import request


def BenchmarkTest32562():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    return render_template_string(data)
