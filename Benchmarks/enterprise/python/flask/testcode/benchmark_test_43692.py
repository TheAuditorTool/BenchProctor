# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest43692():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    return redirect(str(data))
