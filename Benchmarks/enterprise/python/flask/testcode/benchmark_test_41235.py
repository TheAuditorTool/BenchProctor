# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest41235():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    return redirect(str(json_value))
