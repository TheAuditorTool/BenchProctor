# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request
from flask import redirect
import urllib.parse


def BenchmarkTest00840():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
