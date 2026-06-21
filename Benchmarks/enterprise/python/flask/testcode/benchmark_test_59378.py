# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest59378():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
