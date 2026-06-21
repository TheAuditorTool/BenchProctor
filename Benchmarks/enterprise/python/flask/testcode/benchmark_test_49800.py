# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from flask import render_template_string


def BenchmarkTest49800():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    return render_template_string('{{ value }}', value=data)
