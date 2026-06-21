# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest33960():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    return render_template_string(data)
