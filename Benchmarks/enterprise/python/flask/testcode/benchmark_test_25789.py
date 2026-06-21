# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest25789():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    processed = data[:64]
    return redirect(str(processed))
