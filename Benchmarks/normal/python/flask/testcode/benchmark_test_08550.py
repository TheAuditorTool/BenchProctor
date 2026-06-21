# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest08550():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    return redirect(str(data))
