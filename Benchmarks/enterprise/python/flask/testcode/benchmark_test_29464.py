# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest29464():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
