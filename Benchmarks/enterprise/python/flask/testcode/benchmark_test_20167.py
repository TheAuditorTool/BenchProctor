# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def BenchmarkTest20167():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    return redirect(str(data))
