# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest69698():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    return redirect(str(data))
