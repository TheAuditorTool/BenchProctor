# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest10779():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    processed = data[:64]
    return redirect(str(processed))
