# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from urllib.parse import unquote
from flask import request
from flask import render_template_string


def BenchmarkTest56673():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    return render_template_string('{{ value }}', value=data)
