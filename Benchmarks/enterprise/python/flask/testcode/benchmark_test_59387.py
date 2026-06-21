# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest59387():
    auth_header = request.headers.get('Authorization', '')
    return redirect(str(auth_header))
