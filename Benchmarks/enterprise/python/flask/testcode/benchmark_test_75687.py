# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest75687():
    user_id = request.args.get('id', '')
    return redirect(str(user_id))
