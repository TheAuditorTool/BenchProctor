# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import json


def BenchmarkTest41621():
    user_id = request.args.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    return render_template_string(data)
