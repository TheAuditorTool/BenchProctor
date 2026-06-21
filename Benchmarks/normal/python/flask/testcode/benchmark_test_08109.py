# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def BenchmarkTest08109():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    return render_template_string(data)
