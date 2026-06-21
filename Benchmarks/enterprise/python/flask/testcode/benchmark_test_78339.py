# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
import json


def BenchmarkTest78339():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    return redirect(str(data))
