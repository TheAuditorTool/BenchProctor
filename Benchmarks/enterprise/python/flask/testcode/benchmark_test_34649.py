# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest34649():
    header_value = request.headers.get('X-Custom-Header', '')
    return redirect(str(header_value))
