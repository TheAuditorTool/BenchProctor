# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest54807():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    return redirect(str(data))
