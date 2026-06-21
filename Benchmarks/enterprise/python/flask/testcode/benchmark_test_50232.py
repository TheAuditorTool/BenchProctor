# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest50232():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    return render_template_string('safe block: {{ value }}', value=data)
