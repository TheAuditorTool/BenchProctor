# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def BenchmarkTest20558():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return render_template_string('{{ value }}', value=data)
