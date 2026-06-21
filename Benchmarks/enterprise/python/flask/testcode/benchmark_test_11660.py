# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest11660():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    return redirect(str(data))
