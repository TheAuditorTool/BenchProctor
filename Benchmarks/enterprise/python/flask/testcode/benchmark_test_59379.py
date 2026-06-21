# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest59379():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
