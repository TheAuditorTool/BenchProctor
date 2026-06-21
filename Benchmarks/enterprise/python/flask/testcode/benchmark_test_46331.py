# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest46331():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    return redirect(str(data))
