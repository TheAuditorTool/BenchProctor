# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest33622():
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
